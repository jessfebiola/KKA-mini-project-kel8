import pygame
from pathlib import Path


# ==================================================
# DATA LEVEL
# MEMBER 2
# ==================================================

LEVELS = {

    1: {
        "tiles": {
            (0,0): "normal",
            (1,0): "normal",
            (2,0): "normal",
            (3,0): "normal",

            (0,1): "normal",
            (1,1): "normal",
            (2,1): "normal",
            (3,1): "normal",
            (4,1): "normal",
            (5,1): "normal",

            (0,2): "normal",
            (1,2): "normal",
            (2,2): "normal",
            (3,2): "normal",
            (4,2): "normal",
            (5,2): "normal",
            (6,2): "normal",
            (7,2): "normal",
            (8,2): "normal",
            (9,2): "normal",

            (1,3): "normal",
            (2,3): "normal",
            (3,3): "normal",
            (4,3): "normal",
            (5,3): "normal",
            (6,3): "normal",
            (7,3): "normal",
            (8,3): "normal",
            (9,3): "normal",

            (5,4): "normal",
            (6,4): "normal",
            (7,4): "goal",
            (8,4): "normal",
            (9,4): "normal",

            (6,5): "normal",
            (7,5): "normal",
            (8,5): "normal"
        },
        "start": (1,1),
        "goal": (7,4)
    },

    2: {
        "tiles": {
            (6,0): "normal",
            (7,0): "normal",
            (8,0): "normal",
            (9,0): "normal",
            (12,0): "normal",
            (13,0): "normal",
            (14,0): "normal",

            (0,1): "normal",
            (1,1): "normal",
            (2,1): "normal",
            (3,1): "normal",
            (6,1): "normal",
            (7,1): "normal",
            (8,1): "x",
            (9,1): "normal",
            (12,1): "normal",
            (13,1): "goal",
            (14,1): "normal",

            (0,2): "normal",
            (1,2): "normal",
            (2,2): "o",
            (3,2): "normal",
            (6,2): "normal",
            (7,2): "normal",
            (8,2): "normal",
            (9,2): "normal",
            (12,2): "normal",
            (13,2): "normal",
            (14,2): "normal",

            (0,3): "normal",
            (1,3): "normal",
            (2,3): "normal",
            (3,3): "normal",
            (6,3): "normal",
            (7,3): "normal",
            (8,3): "normal",
            (9,3): "normal",
            (12,3): "normal",
            (13,3): "normal",
            (14,3): "normal",

            (0,4): "normal",
            (1,4): "normal",
            (2,4): "normal",
            (3,4): "normal",
            (4,4): "bridge",
            (5,4): "bridge",
            (6,4): "normal",
            (7,4): "normal",
            (8,4): "normal",
            (9,4): "normal",
            (10,4): "bridge",
            (11,4): "bridge",
            (12,4): "normal",
            (13,4): "normal",
            (14,4): "normal",

            (0,5): "normal",
            (1,5): "normal",
            (2,5): "normal",
            (3,5): "normal",
            (6,5): "normal",
            (7,5): "normal",
            (8,5): "normal",
            (9,5): "normal"
        },
        "start": (1,4),
        "goal": (13,1)
    },

    3: {
        "tiles": {
            (6,0): "normal",
            (7,0): "normal",
            (8,0): "normal",
            (9,0): "normal",
            (10,0): "normal",
            (11,0): "normal",
            (12,0): "normal",

            (0,1): "normal",
            (1,1): "normal",
            (2,1): "normal",
            (3,1): "normal",
            (6,1): "normal",
            (7,1): "normal",
            (8,1): "normal",
            (11,1): "normal",
            (12,1): "normal",

            (0,2): "normal",
            (1,2): "normal",
            (2,2): "normal",
            (3,2): "normal",
            (4,2): "normal",
            (5,2): "normal",
            (6,2): "normal",
            (7,2): "normal",
            (8,2): "normal",
            (11,2): "normal",
            (12,2): "normal",
            (13,2): "normal",
            (14,2): "normal",

            (0,3): "normal",
            (1,3): "normal",
            (2,3): "normal",
            (3,3): "normal",
            (11,3): "normal",
            (12,3): "normal",
            (13,3): "goal",
            (14,3): "normal",

            (0,4): "normal",
            (1,4): "normal",
            (2,4): "normal",
            (3,4): "normal",
            (11,4): "normal",
            (12,4): "normal",
            (13,4): "normal",
            (14,4): "normal",

            (12,5): "normal",
            (13,5): "normal",
            (14,5): "normal"
        },
        "start": (1,3),
        "goal": (13,3)
    }
}


# ==================================================
# MEMANGGIL ASSET
# MEMBER 2
# ==================================================

ASSET_DIR = Path(__file__).parent / "assets"

# Menyimpan gambar yang sudah dipanggil
ASSETS = {}
TILE_CACHE = {}
ASSET_SCALE_CACHE = {}


def load_assets():

    nama_assets = [
        # Background
        "bg landing",
        "bg pilih level",
        "bg lvl 1",
        "bg lvl 2",
        "bg lvl 3",
        "bg party",

        # Background Jumpscare
        "bg js lvl 1",
        "bg js lvl 2",
        "bg js lvl 3",

        # Block dan tile
        "blok berdiri",
        "blok tidur",
        "blok lantai",
        "blok lantai bridge",
        "blok lantai goal",
        "blok lantai o",
        "blok lantai x",

        # Tombol Landing
        "start",
        "start hover",

        # Pilihan level
        "pilih level",
        "stage 1 idle",
        "stage 1 selected",
        "stage 2 idle",
        "stage 2 selected",
        "stage 2 locked",
        "stage 3 idle",
        "stage 3 selected",
        "stage 3 locked",

        # Tombol Solver
        "bfs idle",
        "bfs selected",
        "dfs idle",
        "dfs selected",
        "ucs idle",
        "ucs selected",
        "solve",

        # Panel dan informasi
        "puzzle guide",
        "solver performance",

        # Tampilan Win dan Lose
        "menang",
        "kalah",

        # Logo dan tulisan
        "putih",
        "roll to vivat biru",
        "roll to vivat kuning",

        # Asset tambahan
        "jahim",
        "lantai party"
    ]

    for nama in nama_assets:

        file = next(
            (f for f in ASSET_DIR.iterdir()
             if f.is_file() and f.stem == nama),
            None
        )

        if file is not None:
            ASSETS[nama] = pygame.image.load(
                str(file)
            ).convert_alpha()

        else:
            print(f"Asset tidak ditemukan: {nama}")


# ==================================================
# MENGATUR POSISI DAN UKURAN ASSET
# MEMBER 2
# ==================================================

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1024

BACKGROUND_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_ASSETS = {
    1: "bg lvl 1",
    2: "bg lvl 2",
    3: "bg lvl 3"
}

JUMPSCARE_BACKGROUND_ASSETS = {
    1: "bg js lvl 1",
    2: "bg js lvl 2",
    3: "bg js lvl 3"
}


ASSET_LAYOUT = {

    # =========================
    # LANDING PAGE
    # =========================

    "roll to vivat kuning": {
        "pos": (295, 165),
        "size": (850, 118)
    },

    "roll to vivat biru": {
        "pos": (295, 165),
        "size": (850, 118)
    },

    "jahim": {
        "pos": (545, 300),
        "size": (350, 420)
    },
    "start": {
    "pos": (586, 775),
    "size": (267, 55)
    },

    "start hover": {
        "pos": (560, 748),
        "size": (319, 108)
    },


    # =========================
    # LEVEL SELECTION
    # =========================

    "pilih level": {
        "pos": (345, 145),
        "size": (750, 90)
    },

    "stage 1 idle": {
        "pos": (0, 370),
        "size": (600, 600)
    },

    "stage 1 selected": {
        "pos": (0, 370),
        "size": (600, 600)
    },

    "stage 2 idle": {
        "pos": (420, 260),
        "size": (600, 600)
    },

    "stage 2 locked": {
        "pos": (420, 260),
        "size": (600, 600)
    },

    "stage 2 selected": {
        "pos": (420, 260),
        "size": (600, 600)
    },

    "stage 3 idle": {
        "pos": (840, 170),
        "size": (600, 600)
    },

    "stage 3 locked": {
        "pos": (840, 170),
        "size": (600, 600)
    },

    "stage 3 selected": {
        "pos": (840, 170),
        "size": (600, 600)
    },


    # =========================
    # GAMEPLAY - SOLVER BUTTONS
    # =========================

    "solve": {
        "pos": (1212, 30),
        "size": (198, 69)
    },

    "bfs idle": {
        "pos": (28, 558),
        "size": (138, 54)
    },

    "bfs selected": {
        "pos": (28, 558),
        "size": (138, 54)
    },

    "dfs idle": {
        "pos": (28, 628),
        "size": (138, 54)
    },

    "dfs selected": {
        "pos": (28, 628),
        "size": (138, 54)
    },

    "ucs idle": {
        "pos": (28, 698),
        "size": (138, 54)
    },

    "ucs selected": {
        "pos": (28, 698),
        "size": (138, 54)
    },


    # =========================
    # GAMEPLAY - INFORMATION PANEL
    # =========================

    "puzzle guide": {
        "pos": (28, 768),
        "size": (373, 226)
    },

    "solver performance": {
        "pos": (440, 375),
        "size": (560, 270)
    },

    # =========================
    # GAMEPLAY - BOARD
    # =========================

    # Posisi kiri atas papan permainan
    "blok lantai": (430, 250),

    # Ukuran satu tile
    "tile_size": 64,

    # Block berdiri
    "blok berdiri": {
        "pos": (0, 0),
        "size": (64, 64)
    },

    # Block tidur horizontal
    "blok tidur": {
        "pos": (0, 0),
        "size": (128, 64)
    },

    # Block tidur vertikal
    "blok tidur vertikal": {
        "pos": (0, 0),
        "size": (64, 128)
    },


    # =========================
    # WIN / LOSE
    # =========================

    "menang": {
        # Asset asli 462 x 129 (rasio 3.58:1).
        # Ukuran ini mempertahankan rasio sehingga tulisan tidak penyet.
        "pos": (350, 409),
        "size": (740, 207)
    },


    # =========================
    # PARTY PAGE
    # =========================

    "lantai party": {
        "pos": (300, 500),
        "size": (840, 400)
    }
}


# Mengambil ukuran tile dari ASSET_LAYOUT
TILE_SIZE = ASSET_LAYOUT["tile_size"]


TILE_ASSETS = {
    "normal": "blok lantai",
    "bridge": "blok lantai bridge",
    "goal": "blok lantai goal",
    "o": "blok lantai o",
    "x": "blok lantai x"
}


BLOCK_ASSETS = {
    "standing": {
        "name": "blok berdiri",
        "size": (64, 64)
    },

    "sleeping": {
        "name": "blok tidur",
        "size": (128, 64)
    }
}


PAGE_BACKGROUND_ASSETS = {
    "landing": "bg landing",
    "level_select": "bg pilih level",
    "party": "bg party"
}


# ==================================================
# FUNGSI BANTUAN TAMPILAN
# ==================================================

# Menggambar asset berdasarkan konfigurasi layout
def gambar_asset(screen, nama, layout_key):

    if nama not in ASSETS:
        return

    if layout_key not in ASSET_LAYOUT:
        return

    layout = ASSET_LAYOUT[layout_key]

    posisi = layout["pos"]
    ukuran = layout["size"]

    gambar = ASSETS[nama]

    if ukuran is not None:
        # Asset menu disesuaikan proporsional (tidak penyet).
        if nama in {"roll to vivat kuning", "roll to vivat biru", "jahim", "pilih level", "start", "start hover"} or nama.startswith("stage "):
            w, h = gambar.get_size()
            faktor = min(ukuran[0] / w, ukuran[1] / h)
            ukuran = (max(1, round(w * faktor)), max(1, round(h * faktor)))
            posisi = (posisi[0] + (layout["size"][0] - ukuran[0]) // 2,
                      posisi[1] + (layout["size"][1] - ukuran[1]) // 2)
        key = (nama, tuple(ukuran))
        if key not in ASSET_SCALE_CACHE:
            ASSET_SCALE_CACHE[key] = pygame.transform.smoothscale(gambar, ukuran)
        gambar = ASSET_SCALE_CACHE[key]

    screen.blit(gambar, posisi)


# Menggambar background memenuhi layar
def gambar_background(screen, nama):

    if nama not in ASSETS:
        return

    key = (nama, screen.get_size())
    if key not in ASSET_SCALE_CACHE:
        ASSET_SCALE_CACHE[key] = pygame.transform.smoothscale(ASSETS[nama], screen.get_size())
    screen.blit(ASSET_SCALE_CACHE[key], (0, 0))


# Posisi mouse dalam koordinat desain 1440x1024.
VIRTUAL_MOUSE_POS = (-100, -100)

def set_virtual_mouse_pos(pos):
    global VIRTUAL_MOUSE_POS
    VIRTUAL_MOUSE_POS = pos

# Mengecek posisi kursor pada tombol
def cek_hover(layout_key):

    if layout_key not in ASSET_LAYOUT:
        return False

    layout = ASSET_LAYOUT[layout_key]

    posisi = layout["pos"]
    ukuran = layout["size"]

    if ukuran is None:
        return False

    area_tombol = pygame.Rect(posisi, ukuran)

    return area_tombol.collidepoint(
        VIRTUAL_MOUSE_POS
    )


# Menampilkan teks
def gambar_teks(screen, tulisan, posisi, ukuran=28):

    font = pygame.font.Font(None, ukuran)

    teks = font.render(
        str(tulisan),
        True,
        (255, 255, 255)
    )

    screen.blit(teks, posisi)


# ==================================================
# MENAMPILKAN LANDING
# ==================================================

def draw_landing(screen):

    # Menampilkan background Landing
    gambar_background(screen, "bg landing")

    # Menampilkan logo game
    gambar_asset(
        screen,
        "roll to vivat kuning",
        "roll to vivat kuning"
    )
    # Tmbahin jahim
    gambar_asset(screen, "jahim", "jahim")

    # Menampilkan tombol Start sesuai kondisi hover
    if cek_hover("start"):
        gambar_asset(
            screen,
            "start hover",
            "start hover"
        )

    else:
        gambar_asset(
            screen,
            "start",
            "start"
        )


# ==================================================
# MENAMPILKAN LEVEL SELECTION
# ==================================================

def draw_level_selection(screen, data_game):

    # Menampilkan background Level Selection
    gambar_background(screen, "bg pilih level")

    # Menampilkan judul Pilih Level
    gambar_asset(
        screen,
        "pilih level",
        "pilih level"
    )

    # Mengambil level tertinggi yang sudah terbuka
    unlocked_level = data_game.get(
        "unlocked_level", 1
    )

    # Mengambil level yang sedang dipilih
    selected_level = data_game.get("level")

    # Menampilkan setiap stage
    for level in range(1, 4):

        if level > unlocked_level:
            nama_asset = f"stage {level} locked"

        elif level == selected_level:
            nama_asset = f"stage {level} selected"

        else:
            nama_asset = f"stage {level} idle"

        gambar_asset(
            screen,
            nama_asset,
            nama_asset
        )


# ==================================================
# MENGGAMBAR TILE
# ==================================================

def draw_tiles(screen, tiles, origin=None):

    # Mengambil posisi awal papan
    if origin is None:
        origin = ASSET_LAYOUT["blok lantai"]
    tile_size = TILE_SIZE

    # Menggambar tile berdasarkan koordinat LEVELS
    for koordinat, jenis in tiles.items():

        x, y = koordinat

        posisi = (
            origin[0] + x * tile_size,
            origin[1] + y * tile_size
        )

        nama_asset = TILE_ASSETS.get(jenis)

        if nama_asset not in ASSETS:
            continue

        # Menyimpan hasil resize agar tidak diulang setiap frame
        cache_key = (nama_asset, tile_size)

        if cache_key not in TILE_CACHE:
            TILE_CACHE[cache_key] = pygame.transform.smoothscale(
                ASSETS[nama_asset],
                (tile_size, tile_size)
            )

        gambar = TILE_CACHE[cache_key]

        screen.blit(gambar, posisi)
        # Goal Level 2 menggunakan satu petak hijau, bukan biru.
        if jenis == "goal":
            inset = max(4, tile_size // 12)
            kotak = pygame.Rect(posisi[0] + inset, posisi[1] + inset,
                                tile_size - 2 * inset, tile_size - 2 * inset)
            pygame.draw.rect(screen, (36, 170, 73), kotak, border_radius=7)
            pygame.draw.rect(screen, (19, 93, 46), kotak, 3, border_radius=7)


# ==================================================
# MENGGAMBAR BLOCK
# ==================================================

def draw_block(screen, state, origin=None):


    if state is None:
        return

    (x1, y1), (x2, y2) = state

    if origin is None:
        origin = ASSET_LAYOUT["blok lantai"]
    tile_size = TILE_SIZE

    # Block berdiri
    if (x1, y1) == (x2, y2):
        gambar = ASSETS["blok berdiri"]
        ukuran = (tile_size, tile_size)

    # Block tidur horizontal
    elif y1 == y2:
        gambar = ASSETS["blok tidur"]
        ukuran = (tile_size * 2, tile_size)

    # Block tidur vertikal
    else:
        gambar = pygame.transform.rotate(
            ASSETS["blok tidur"], 90
        )
        ukuran = (tile_size, tile_size * 2)

    gambar = pygame.transform.smoothscale(gambar, ukuran)

    x = origin[0] + min(x1, x2) * tile_size
    y = origin[1] + min(y1, y2) * tile_size

    screen.blit(gambar, (x, y))



# ==================================================
# MENAMPILKAN TOMBOL SOLVER
# ==================================================

def draw_solver_buttons(screen, data_game):

    # Mengambil algoritma yang dipilih
    solver_method = data_game.get("solver_method")

    daftar_solver = {
        "BFS": ("bfs idle", "bfs selected"),
        "DFS": ("dfs idle", "dfs selected"),
        "UCS": ("ucs idle", "ucs selected")
    }

    # Menampilkan tombol BFS, DFS, dan UCS
    for nama, asset in daftar_solver.items():

        if solver_method == nama:
            nama_asset = asset[1]

        else:
            nama_asset = asset[0]

        gambar_asset(
            screen,
            nama_asset,
            nama_asset
        )

    # Menampilkan tombol Solve
    gambar_asset(
        screen,
        "solve",
        "solve"
    )


# ==================================================
# MENAMPILKAN PUZZLE GUIDE
# ==================================================

def draw_puzzle_guide(screen):

    gambar_asset(
        screen,
        "puzzle guide",
        "puzzle guide"
    )


# ==================================================
# MENAMPILKAN SOLVER PERFORMANCE
# ==================================================

def draw_solver_performance(screen, data_game):
    """Tampilkan panel statistik di tengah tanpa teks saling bertumpuk."""
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))

    # Asset asli sudah berisi judul dan label statistik.
    gambar_asset(screen, "solver performance", "solver performance")

    hasil = data_game.get("solver_stats", {})
    algorithm = hasil.get("algorithm") or data_game.get("solver_method") or "-"
    path = hasil.get("path", []) or []
    path_length = hasil.get("path_length", len(path))
    discovered = hasil.get("discovered", "-")
    expanded = hasil.get("expanded", "-")
    elapsed = hasil.get("time", 0) or 0

    nilai_statistik = [
        str(algorithm),
        str(path_length),
        str(discovered),
        str(expanded),
        f"{float(elapsed):.6f} s",
    ]

    # Titik awal nilai relatif terhadap posisi panel (bukan layar).
    panel = ASSET_LAYOUT["solver performance"]
    px, py = panel["pos"]
    pw, ph = panel["size"]
    # Kolom nilai di sisi kanan label bawaan gambar.
    value_x = px + int(pw * 0.62)
    start_y = py + int(ph * 0.28)
    line_gap = int(ph * 0.132)
    font = pygame.font.Font(None, 25)

    for index, value in enumerate(nilai_statistik):
        teks = font.render(value, True, (255, 255, 255))
        screen.blit(teks, (value_x, start_y + index * line_gap))


# ==================================================
# MENAMPILKAN GAMEPLAY
# ==================================================

def draw_gameplay(screen, data_game):

    # Mengambil data level yang sedang dimainkan
    level = data_game.get("level")

    if level not in LEVELS:
        return

    data_level = LEVELS[level]

    # Posisi papan per level mengikuti gambar referensi; koordinat game tidak berubah.
    board_origin = {
        1: (375, 359),
        2: (257, 323),
        3: (230, 317),
    }.get(level, ASSET_LAYOUT["blok lantai"])

    # Menampilkan background sesuai level
    gambar_background(
        screen,
        BACKGROUND_ASSETS[level]
    )

    # Menggambar tile berdasarkan koordinat
    draw_tiles(
        screen,
        {pos: ("normal" if kind == "bridge" else kind) for pos, kind in data_level["tiles"].items()
         if kind != "bridge" or (
             (pos[0] in (4, 5) and data_game.get("bridge_o_open", False)) or
             (pos[0] in (10, 11) and data_game.get("bridge_x_open", False))
         )},
        origin=board_origin
    )

    # Menggambar block sesuai posisi dan orientasi
    if data_game.get("posisi_block") is not None:
        draw_block(
            screen,
            data_game["posisi_block"],
            origin=board_origin
        )

    # Menampilkan tombol Solver
    draw_solver_buttons(screen, data_game)

    # Menampilkan Puzzle Guide
    draw_puzzle_guide(screen)

    # Menampilkan Solver Performance
    if data_game.get("solver_show_performance", False):
        draw_solver_performance(screen, data_game)


# ==================================================
# MENAMPILKAN WIN DAN JUMPSCARE
# ==================================================

def draw_win(screen):

    # Menampilkan tampilan Congratulations
    gambar_asset(
        screen,
        "menang",
        "menang"
    )


def draw_jumpscare(screen, data_game):

    # Mengambil level yang sedang dimainkan
    level = data_game.get("level")

    nama_background = JUMPSCARE_BACKGROUND_ASSETS.get(level)

    if nama_background:
        gambar_background(
            screen,
            nama_background
        )


# ==================================================
# MENAMPILKAN PARTY
# ==================================================

def draw_party(screen):
    """Tampilan akhir Level 3, menjaga proporsi seluruh asset."""
    lebar_layar, tinggi_layar = screen.get_size()

    # Background memenuhi layar dengan crop tengah, tanpa penyet.
    background = ASSETS.get("bg party")
    if background is not None:
        bw, bh = background.get_size()
        skala_bg = max(lebar_layar / bw, tinggi_layar / bh)
        ukuran_bg = (max(1, round(bw * skala_bg)),
                     max(1, round(bh * skala_bg)))
        key_bg = ("bg party cover", ukuran_bg)
        if key_bg not in ASSET_SCALE_CACHE:
            ASSET_SCALE_CACHE[key_bg] = pygame.transform.smoothscale(
                background, ukuran_bg
            )
        gambar_bg = ASSET_SCALE_CACHE[key_bg]
        posisi_bg = ((lebar_layar - ukuran_bg[0]) // 2,
                     (tinggi_layar - ukuran_bg[1]) // 2)
        screen.blit(gambar_bg, posisi_bg)
    else:
        screen.fill((18, 39, 70))

    # Kolase party: tampilkan sebesar mungkin sambil mempertahankan
    # perbandingan lebar dan tinggi asli (tidak gepeng/penyet).
    kolase = ASSETS.get("lantai party")
    if kolase is not None:
        kw, kh = kolase.get_size()
        area_w = int(lebar_layar * 0.64)
        area_h = int(tinggi_layar * 0.60)
        skala = min(area_w / kw, area_h / kh)
        ukuran = (max(1, round(kw * skala)),
                  max(1, round(kh * skala)))
        key_kolase = ("lantai party proporsional", ukuran)
        if key_kolase not in ASSET_SCALE_CACHE:
            ASSET_SCALE_CACHE[key_kolase] = pygame.transform.smoothscale(
                kolase, ukuran
            )
        gambar_kolase = ASSET_SCALE_CACHE[key_kolase]
        posisi = gambar_kolase.get_rect(
            center=(lebar_layar // 2, tinggi_layar // 2)
        )
        screen.blit(gambar_kolase, posisi)


# ==================================================
# MENAMPILKAN PAGE SESUAI KONDISI GAME
# ==================================================

def draw_page(screen, data_game):

    # Memanggil asset jika belum dimuat
    if not ASSETS:
        load_assets()

    page = data_game["page"]

    if page == "landing":
        draw_landing(screen)

    elif page == "level_select":
        draw_level_selection(
            screen,
            data_game
        )

    elif page == "gameplay":
        draw_gameplay(
            screen,
            data_game
        )

    elif page == "win":
        draw_gameplay(
            screen,
            data_game
        )
        draw_win(screen)

    elif page == "jumpscare":
        draw_jumpscare(
            screen,
            data_game
        )

    elif page == "party":
        draw_party(screen)