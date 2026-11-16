import pygame
from pathlib import Path
from collections import deque
import heapq
import time

# Mengambil fungsi tampilan dan data level
# dari game_render.py
from game_render import draw_page, LEVELS, set_virtual_mouse_pos

# Mengambil fungsi mekanisme game
# dari game_logic.py
from game_logic import move_block, check_fall, check_win, update_bridges

# Mengambil algoritma pencarian
# dari solver.py
from solver import bfs, dfs, ucs
import fireworks


# ==================================================
# PERSIAPAN GAME
# MEMBER 1
# ==================================================

pygame.init()
pygame.mixer.init()

# Ukuran layar mengikuti frame Figma
# Render internal tetap 1440x1024 agar layout game/solver tidak berubah.
DESIGN_W, DESIGN_H = 1440, 1024
WINDOW_W, WINDOW_H = 960, 680
screen = pygame.Surface((DESIGN_W, DESIGN_H))
window = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.RESIZABLE)

def view_rect():
    ww, wh = window.get_size()
    scale = min(ww / DESIGN_W, wh / DESIGN_H)
    w, h = round(DESIGN_W * scale), round(DESIGN_H * scale)
    return pygame.Rect((ww-w)//2, (wh-h)//2, w, h)

def to_design_pos(pos):
    rect = view_rect()
    if not rect.collidepoint(pos):
        return (-1000, -1000)
    return (int((pos[0]-rect.x) * DESIGN_W / rect.width),
            int((pos[1]-rect.y) * DESIGN_H / rect.height))


# Judul game
pygame.display.set_caption("Roll to Vivat")

# Mengatur FPS
clock = pygame.time.Clock()

# Data permainan
data_game = {
    "page": "landing",          # Page yang sedang dibuka
    "level": None,              # Level yang dipilih
    "posisi_block": None,       # Posisi block saat ini
    "status": "playing",        # Kondisi permainan
    "unlocked_level":1,
    "bridge_o_open": False, "bridge_x_open": False,

    # Data Solver
    "solver_method": None,      # Algoritma yang dipilih: BFS, DFS, UCS
    "solver_result": [],        # Hasil urutan gerakan Solver
    "solver_index": 0,          # Urutan gerakan yang sedang dijalankan
    "solver_running": False,    # Status Solver
    "solver_last_time": 0,     # Waktu gerakan Solver terakhir
    "solver_stats":{},
    "solver_show_performance":False
}

# ==================================================
# MENGATUR SOUND
# MEMBER 1
# ==================================================
ASSETS_DIR = Path(__file__).parent / "assets" / "bgsound"

def cari_sound(nama):
    for file in ASSETS_DIR.rglob("*"):

        if file.is_file() and file.stem == nama:
            return file

    print(f"Sound tidak ditemukan: {nama}")
    return None

SOUND_GAME = cari_sound("bgsound full 3")
SOUND_PARTY = cari_sound("bgsound party")

# Menyimpan musik yang sedang aktif agar atur_sound() tidak NameError
musik_aktif = None

SOUND_JUMPSCARE = {
    1: cari_sound("bgsound js lvl 1"),
    2: cari_sound("bgsound js lvl 2"),
    3: cari_sound("bgsound js lvl 3")
}

def atur_sound():

    global musik_aktif

    # Memilih musik berdasarkan halaman
    if data_game["page"] == "gameplay":
        musik_baru = SOUND_GAME

    elif data_game["page"] == "party":
        musik_baru = SOUND_PARTY

    else:
        musik_baru = None

    # Mengganti musik jika halaman berubah
    if musik_baru != musik_aktif:

        pygame.mixer.music.stop()
        musik_aktif = musik_baru

        if musik_aktif is not None:

            pygame.mixer.music.load(str(musik_aktif))
            pygame.mixer.music.play(-1)


def putar_jumpscare():

    # Mengambil jumpscare sesuai level
    level = data_game["level"]
    sound = SOUND_JUMPSCARE.get(level)

    if sound is not None:

        # Menghentikan background music
        pygame.mixer.music.stop()

        # Memutar sound jumpscare
        pygame.mixer.Sound(str(sound)).play()



# ==================================================
# MENGATUR NAVIGASI
# MEMBER 1
# ==================================================

def mulai_level(level):
    start = LEVELS[level]["start"]
    data_game.update({
        "page": "gameplay", "level": level,
        "posisi_block": (start, start), "status": "playing",
        "solver_method": None, "solver_result": [], "solver_index": 0,
        "solver_running": False, "solver_last_time": 0,
        "solver_stats": {}, "solver_show_performance": False,
        "bridge_o_open": False, "bridge_x_open": False
    })


# LEVEL 2: koordinat internal papan (x, y), logic lama memakai (baris, kolom).
def gerakkan_xy(state, arah):
    return move_block(state, arah)


def normalisasi(state):
    return tuple(sorted(state))


def jembatan_aktif(pos, o_open, x_open):
    x, y = pos
    if y != 4:
        return True
    if x in (4, 5):
        return o_open
    if x in (10, 11):
        return x_open
    return True


def posisi_aman_level2(state, o_open, x_open):
    tiles = LEVELS[2]["tiles"]
    return all(pos in tiles and jembatan_aktif(pos, o_open, x_open) for pos in state)


def tekan_switch_level2(state, o_open, x_open, sebelumnya=None):
    # Tombol hanya aktif saat baru diinjak, bukan setiap frame.
    sebelum = set(sebelumnya or ())
    sekarang = set(state)
    if (2, 2) in sekarang and (2, 2) not in sebelum:
        o_open = True
    if state[0] == state[1] == (8, 1) and sebelumnya != state:
        x_open = True
    return o_open, x_open


def terapkan_gerakan(state, arah, o_open, x_open):
    baru = normalisasi(gerakkan_xy(state, arah))
    o_open, x_open = tekan_switch_level2(baru, o_open, x_open, state)
    return baru, o_open, x_open


def cari_solusi_level2(start_state, metode, o_open=False, x_open=False):
    # BFS/DFS/UCS dengan state jembatan; solver.py tetap milik Member 4.
    awal_waktu = time.perf_counter()
    awal = (normalisasi(start_state), o_open, x_open)
    parents = {awal: None}
    expanded = 0
    urutan = ("UP", "DOWN", "LEFT", "RIGHT")
    if metode == "UCS":
        frontier = [(0, 0, awal)]
        distances = {awal: 0}
        counter = 0
    else:
        frontier = deque([awal]) if metode == "BFS" else [awal]
    while frontier:
        if metode == "UCS":
            biaya, _, node = heapq.heappop(frontier)
            if biaya != distances[node]:
                continue
        elif metode == "BFS":
            node = frontier.popleft()
        else:
            node = frontier.pop()
        state, bo, bx = node
        expanded += 1
        if state[0] == state[1] == LEVELS[2]["goal"]:
            path = []
            while parents[node] is not None:
                parent, arah = parents[node]
                path.append(arah)
                node = parent
            path.reverse()
            return {"algorithm": metode, "path": path, "discovered": len(parents),
                    "expanded": expanded, "time": time.perf_counter()-awal_waktu}
        for arah in urutan:
            baru, no, nx = terapkan_gerakan(state, arah, bo, bx)
            if not posisi_aman_level2(baru, no, nx):
                continue
            next_node = (baru, no, nx)
            if next_node in parents:
                continue
            parents[next_node] = (node, arah)
            if metode == "UCS":
                counter += 1
                distances[next_node] = biaya + 1
                heapq.heappush(frontier, (biaya + 1, counter, next_node))
            else:
                frontier.append(next_node)
    return {"algorithm": metode, "path": [], "discovered": len(parents),
            "expanded": expanded, "time": time.perf_counter()-awal_waktu}


def atur_menu(event):
    # Keyboard: ESC untuk kembali, R untuk restart
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            page = data_game["page"]
            if page == "level_select":
                data_game["page"] = "landing"
            elif page in ("gameplay", "win", "jumpscare", "party"):
                data_game["page"] = "level_select"
            data_game["solver_running"] = False
            data_game["solver_show_performance"] = False
            return

        if event.key == pygame.K_r:
            if data_game["page"] in ("gameplay", "win", "jumpscare"):
                level = data_game["level"]
                if level in LEVELS:
                    mulai_level(level)
                    print(f"RESTART LEVEL {level}")
            return

        # Enter pada halaman kemenangan: lanjut ke level berikutnya
        if event.key == pygame.K_RETURN and data_game["page"] == "win":
            level = data_game["level"]
            if level < max(LEVELS):
                data_game["unlocked_level"] = max(data_game["unlocked_level"], level + 1)
                mulai_level(level + 1)
            else:
                # Jangan otomatis membuka Party dari kemenangan solver.
                if not data_game.get("solver_result"):
                    data_game["page"] = "party"
                    fireworks.reset()
                else:
                    data_game["page"] = "level_select"
            return

    if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
        return

    mouse_x, mouse_y = event.pos
    if data_game["page"] == "landing":
        if pygame.Rect(586, 775, 267, 55).collidepoint(mouse_x, mouse_y):
            data_game["page"] = "level_select"
            print("START BERHASIL DIKLIK!")
        return

    if data_game["page"] == "level_select":
        # Area klik mengikuti posisi ikon stage yang diperbesar.
        tombol_level = {
            1: pygame.Rect(175, 540, 250, 325),
            2: pygame.Rect(595, 540, 250, 325),
            3: pygame.Rect(1015, 540, 250, 325)
        }
        for level, area in tombol_level.items():
            if area.collidepoint(mouse_x, mouse_y):
                if level > data_game["unlocked_level"]:
                    print(f"Level {level} masih terkunci!")
                    return
                mulai_level(level)
                print(f"MASUK LEVEL {level}")
                return


# ==================================================
# MENGATUR GERAKAN PEMAIN
# MEMBER 3
# ==================================================

def gerak_pemain(event):

    if event.type != pygame.KEYDOWN:
        return
    if data_game["page"] != "gameplay":
        return
    if data_game["solver_running"]:
        return

    if event.key == pygame.K_UP:
        direction = "UP"
    elif event.key == pygame.K_DOWN:
        direction = "DOWN"
    elif event.key == pygame.K_LEFT:
        direction = "LEFT"
    elif event.key == pygame.K_RIGHT:
        direction = "RIGHT"
    else:
        return

    # Mengambil posisi block saat ini
    posisi_sekarang = data_game["posisi_block"]
    # Menghitung posisi block setelah bergerak
    posisi_baru = normalisasi(move_block(posisi_sekarang, direction))
    # Menyimpan posisi baru
    data_game["posisi_block"] = posisi_baru
    # Samakan mekanisme switch dengan solver Level 2.
    if data_game["level"] == 2:
        bo, bx = tekan_switch_level2(
            posisi_baru,
            data_game["bridge_o_open"],
            data_game["bridge_x_open"],
            posisi_sekarang,
        )
        data_game["bridge_o_open"] = bo
        data_game["bridge_x_open"] = bx


def cek_game():

    # Pastikan sedang berada di halaman gameplay
    if data_game["page"] != "gameplay":
        return

    # Ambil data level yang sedang dimainkan
    level = data_game["level"]
    posisi_block = data_game["posisi_block"]

    # Kalau data belum tersedia, hentikan pengecekan
    if level is None or posisi_block is None:
        return

    # Ambil tiles dan goal dari LEVELS
    tiles = LEVELS[level]["tiles"]
    goal = LEVELS[level]["goal"]

    # Cek apakah block jatuh
    if (not posisi_aman_level2(posisi_block, data_game["bridge_o_open"], data_game["bridge_x_open"])
            if level == 2 else check_fall(posisi_block, tiles)):

        data_game["status"] = "lose"
        data_game["page"] = "jumpscare"
        data_game["solver_running"] = False
        data_game["solver_show_performance"] = False

        # Memutar jumpscare sesuai level
        putar_jumpscare()
        return

    # Cek apakah block mencapai goal
    if check_win(posisi_block, goal):
        data_game["unlocked_level"] = max(data_game["unlocked_level"], min(level + 1, max(LEVELS)))

        # Solver selesai: tetap di gameplay agar panel statistik terlihat.
        if data_game.get("solver_method") and data_game.get("solver_result") and data_game["solver_index"] >= len(data_game["solver_result"]):
            data_game["solver_running"] = False
            data_game["solver_show_performance"] = True
            return

        data_game["status"] = "win"
        # Level 3 hanya masuk Party jika diselesaikan secara manual.
        # Solver tetap menampilkan statistiknya, bukan halaman Party.
        if level == 3 and not data_game.get("solver_result"):
            data_game["page"] = "party"
            fireworks.reset()
        else:
            data_game["page"] = "win"
        data_game["solver_running"] = False
        data_game["solver_show_performance"] = False


# ==================================================
# MENGATUR SOLVER
# MEMBER 4
# ==================================================

def pilih_solver(event):
    if data_game["page"] != "gameplay" or data_game["solver_running"]:
        return
    if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
        return

    x, y = event.pos
    tombol = {
        "BFS": pygame.Rect(28, 558, 138, 54),
        "DFS": pygame.Rect(28, 628, 138, 54),
        "UCS": pygame.Rect(28, 698, 138, 54),
    }
    for metode, area in tombol.items():
        if area.collidepoint(x, y):
            data_game["solver_method"] = metode
            data_game["solver_show_performance"] = False
            print(f"Solver dipilih: {metode}")
            return

    if not pygame.Rect(1212, 30, 198, 69).collidepoint(x, y):
        return

    metode = data_game.get("solver_method")
    if metode not in ("BFS", "DFS", "UCS"):
        print("Pilih BFS, DFS, atau UCS terlebih dahulu!")
        return

    level = data_game["level"]
    if level not in LEVELS:
        return

    # game_logic dan solver.py memakai (baris, kolom),
    # sementara LEVELS dan tampilan memakai (x, y).
    state_rc = tuple((y0, x0) for x0, y0 in data_game["posisi_block"])
    level_xy = LEVELS[level]
    level_rc = {
        **level_xy,
        "tiles": {(y0, x0): jenis for (x0, y0), jenis in level_xy["tiles"].items()},
        "goal": (level_xy["goal"][1], level_xy["goal"][0]),
    }

    fungsi = {"BFS": bfs, "DFS": dfs, "UCS": ucs}[metode]
    hasil = (cari_solusi_level2(data_game["posisi_block"], metode,
                              data_game["bridge_o_open"], data_game["bridge_x_open"])
             if level == 2 else fungsi(state_rc, level_rc))
    data_game["solver_stats"] = hasil
    data_game["solver_result"] = hasil.get("path", [])
    data_game["solver_index"] = 0
    data_game["solver_last_time"] = pygame.time.get_ticks()
    data_game["solver_show_performance"] = False
    data_game["solver_running"] = bool(data_game["solver_result"])

    if not data_game["solver_running"]:
        data_game["solver_show_performance"] = True
        print("Tidak ada langkah solver (sudah di goal atau solusi tidak ditemukan).")
    else:
        print(f"{metode}: {len(data_game['solver_result'])} langkah")


def gerak_solver():
    if data_game["page"] != "gameplay" or not data_game["solver_running"]:
        return

    sekarang = pygame.time.get_ticks()
    if sekarang - data_game["solver_last_time"] < 300:
        return

    indeks = data_game["solver_index"]
    langkah = data_game["solver_result"]
    if indeks >= len(langkah):
        data_game["solver_running"] = False
        data_game["solver_show_performance"] = True
        return

    arah = langkah[indeks]
    state_xy = data_game["posisi_block"]
    if data_game["level"] == 2:
        # Solver Level 2 dan game_logic memakai koordinat (x, y).
        data_game["posisi_block"] = normalisasi(move_block(state_xy, arah))
    else:
        # Pertahankan konversi untuk solver.py Level 1/3 yang memakai (row, col).
        state_rc = tuple((y0, x0) for x0, y0 in state_xy)
        hasil_rc = move_block(state_rc, arah)
        data_game["posisi_block"] = tuple((kolom, baris) for baris, kolom in hasil_rc)
    if data_game["level"] == 2:
        bo, bx = tekan_switch_level2(data_game["posisi_block"], data_game["bridge_o_open"], data_game["bridge_x_open"], state_xy)
        data_game["bridge_o_open"], data_game["bridge_x_open"] = bo, bx
    data_game["solver_index"] += 1
    data_game["solver_last_time"] = sekarang

    if data_game["solver_index"] >= len(langkah):
        data_game["solver_running"] = False
        data_game["solver_show_performance"] = True


# ==================================================
# PROGRAM UTAMA
# MENGHUBUNGKAN SEMUA BAGIAN
# ==================================================

running = True

while running:

    # A. MEMBACA INPUT PEMAIN
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((max(600,event.w), max(430,event.h)), pygame.RESIZABLE)

        else:
            # Konversi klik window kecil ke koordinat desain.
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                event = pygame.event.Event(event.type, {**event.dict, "pos": to_design_pos(event.pos)})
            # Member 1: Mengatur navigasi
            atur_menu(event)

            # Member 3: Mengatur gerakan block
            gerak_pemain(event)

            # Member 4: Mengatur pilihan Solver
            pilih_solver(event)

    # B. MENGECEK KONDISI PERMAINAN
    cek_game()

    # C. MENJALANKAN SOLVER
    gerak_solver()

    # D. MENGATUR SOUND
    atur_sound()

    # E. MENAMPILKAN PAGE
    # Memanggil draw_page() dari game_render.py
    set_virtual_mouse_pos(to_design_pos(pygame.mouse.get_pos()))
    draw_page(screen, data_game)
    if data_game["page"] == "party":
        fireworks.draw(screen, pygame.time.get_ticks())

    # F. Skala proporsional dan letterbox agar tidak terpotong/penyet.
    rect = view_rect()
    window.fill((15, 15, 15))
    scaled = pygame.transform.smoothscale(screen, rect.size)
    window.blit(scaled, rect.topleft)
    pygame.display.flip()

    # Membatasi game menjadi 60 FPS
    clock.tick(60)


# Menutup Pygame
pygame.mixer.music.stop()
pygame.quit()
