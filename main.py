import pygame
from pathlib import Path

# Mengambil fungsi tampilan dan data level
# dari game_render.py
from game_render import draw_page, LEVELS

# Mengambil fungsi mekanisme game
# dari game_logic.py
from game_logic import move_block, check_fall, check_win

# Mengambil algoritma pencarian
# dari solver.py
from solver import bfs, dfs, ucs


# ==================================================
# PERSIAPAN GAME
# MEMBER 1
# ==================================================

pygame.init()
pygame.mixer.init()

# Ukuran layar mengikuti frame Figma
screen = pygame.display.set_mode((1440, 1024))

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
SOUND_PARTY = cari_sound("party bgsound")

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

def atur_menu(event):

    # Mengatur tombol Start, Setting, dan Credit.
    # Mengatur perpindahan Landing ke Level Selection.
    # Mengatur pemilihan level.
    # Mengambil data level dari LEVELS di game_render.py.
    # Mengatur posisi awal block ketika level dimulai.
    # Mengatur tombol Back, Restart, dan Next Level.


    pass


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
    posisi_baru = move_block(posisi_sekarang, direction)
    # Menyimpan posisi baru
    data_game["posisi_block"] = posisi_baru

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
    if check_fall(posisi_block, tiles):

        data_game["status"] = "lose"
        data_game["page"] = "jumpscare"
        data_game["solver_running"] = False
        data_game["solver_show_performance"] = False

        # Memutar jumpscare sesuai level
        putar_jumpscare()
        return

    # Cek apakah block mencapai goal
    if check_win(posisi_block, goal):

        data_game["status"] = "win"
        data_game["page"] = "win"
        data_game["solver_running"] = False
        data_game["solver_show_performance"] = False


# ==================================================
# MENGATUR SOLVER
# MEMBER 4
# ==================================================

def pilih_solver(event):

    # Mendeteksi pilihan BFS, DFS, atau UCS.
    # Memanggil algoritma yang dipilih dari solver.py.
    # Mengirim posisi block dan data level.
    # Menyimpan hasil pencarian ke solver_result.
    # Mengatur solver_index menjadi 0.
    # Menjalankan Solver jika solusi ditemukan.

    pass


def gerak_solver():

    # Mengambil gerakan berikutnya dari solver_result.
    # Menjalankan gerakan satu per satu.
    # Memanggil move_block() dari game_logic.py.
    # Memberikan jeda antar gerakan.
    # Menghentikan Solver jika solusi selesai atau game berakhir.

    pass


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

        else:
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
    draw_page(screen, data_game)

    # F. MEMPERBARUI TAMPILAN
    pygame.display.flip()

    # Membatasi game menjadi 60 FPS
    clock.tick(60)


# Menutup Pygame
pygame.mixer.music.stop()
pygame.quit()
