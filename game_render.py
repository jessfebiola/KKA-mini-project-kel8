import pygame


# ==================================================
# DATA LEVEL
# ==================================================

# Menyimpan susunan tile, posisi awal block,
# dan posisi goal setiap level.

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
        "start": (1,1),  # Isi posisi awal block.
        "goal": (7,4)    # Isi posisi goal.
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

# Memanggil background Landing.
# Memanggil background Level Selection.
# Memanggil background setiap Gameplay.
# Memanggil gambar tombol.
# Memanggil gambar tile dan goal.
# Memanggil gambar block sesuai orientasi.
# Memanggil gambar panel, icon, dan font.

from pathlib import Path

# Mengambil lokasi folder assets
ASSET_DIR = Path(__file__).parent / "assets"

# Menyimpan gambar yang sudah dipanggil
ASSETS = {}


# Memanggil seluruh gambar dari folder assets
def load_assets():

    nama_assets = [
        # Background
        "bg landing",
        "bg pilih level",
        "bg lvl 1",
        "bg lvl 2",
        "bg lvl 3",
        "bg party",

        # Background Gameplay
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

        # Mencari file berdasarkan nama tanpa ekstensi
        file = next(
            (f for f in ASSET_DIR.iterdir() if f.stem == nama),
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

# Mengatur posisi dan ukuran background.
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

# Mengatur posisi tombol Start
# Mengatur posisi tombol Solve, BFS, DFS, dan UCS.
# # Mengatur posisi Puzzle Guide.
# Mengatur posisi Solver Performance.
ASSET_LAYOUT = {
    # =========================
    # LANDING PAGE
    # =========================
    "roll to vivat kuning": {
        "pos": (450, 250),
        "size": (540, 250)
    },
    "roll to vivat biru": {
            "pos": (450, 250),
            "size": (540, 250)
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
        "pos": (450, 150),
        "size": (540, 120)
    },
    "stage 1 idle": {
        "pos": (300, 450),
        "size": (220, 220)
    },
    "stage 1 selected": {
        "pos": (300, 450),
        "size": (220, 220)
    },
    "stage 2 idle": {
        "pos": (610, 450),
        "size": (220, 220)
    },
    "stage 2 locked": {
        "pos": (610, 450),
        "size": (220, 220)
    }, 
    "stage 2 selected": {
        "pos": (610, 450),
        "size": (220, 220)
    }, 
    "stage 3 idle": {
        "pos": (920, 450),
        "size": (220, 220)
    },
    "stage 3 locked": {
        "pos": (920, 450),
        "size": (220, 220)
    },
    "stage 3 selected": {
        "pos": (920, 450),
        "size": (220, 220)
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
        "pos": (853, 727),
        "size": (559, 269)
    },

    # Posisi teks pada panel Solver Performance
    "solver_text_0": {
        "pos": (900, 765),
        "size": 26
    },
    "solver_text_1": {
        "pos": (900, 805),
        "size": 26
    },
    "solver_text_2": {
        "pos": (900, 845),
        "size": 26
    },
    "solver_text_3": {
        "pos": (900, 885),
        "size": 26
    },
    "solver_text_4": {
        "pos": (900, 925),
        "size": 26
    },

    # =========================
    # GAMEPLAY - BOARD
    # =========================
    # Posisi kiri atas papan permainan.
    # Ini nilai awal sementara, perlu dicocokkan
    # dengan background gameplay yang sebenarnya.
    "blok lantai": (430, 250),

    # Ukuran satu tile
    "tile_size": 64,

    # Posisi dan ukuran block berdiri
    "blok berdiri": {
        "pos": (0, 0),
        "size": (64, 64)
    },

    # Posisi dan ukuran block tidur horizontal
    "blok tidur": {
        "pos": (0, 0),
        "size": (128, 64)
    },

    # Posisi dan ukuran block tidur vertikal
    "blok berdiri": {
        "pos": (0, 0),
        "size": (64, 128)
    },

    # =========================
    # WIN / LOSE
    # =========================
    "menang": {
        "pos": (400, 250),
        "size": (640, 450)
    },

    # =========================
    # PARTY PAGE
    # =========================
    "lantai party": {
        "pos": (300, 500),
        "size": (840, 400)
    }
}

# Mengatur ukuran dan posisi tile, block, serta goal.
TILE_SIZE = 64

TILE_ASSETS = {
    "normal": "blok lantai",
    "bridge": "blok lantai bridge",
    "goal": "blok lantai goal",
    "o": "blok lantai o",
    "x": "blok lantai x",
    "start": "blok berdiri"
}

BLOCK_ASSETS = {
    "standing": {
        "name": "blok berdiri",
        "size": TILE_SIZE
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
        gambar = pygame.transform.smoothscale(gambar, ukuran)

    screen.blit(gambar, posisi)


# Menggambar background memenuhi layar
def gambar_background(screen, nama):

    if nama not in ASSETS:
        return

    background = pygame.transform.smoothscale(
        ASSETS[nama],
        screen.get_size()
    )

    screen.blit(background, (0, 0))


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

    return area_tombol.collidepoint(pygame.mouse.get_pos())


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

    # Menampilkan background Landing.
    gambar_background(screen, "bg landing")
    # Menampilkan logo game.
    gambar_asset(screen, "putih", "logo_landing")

    # Menampilkan tombol Start sesuai kondisi hover
    if cek_hover("start"):
        gambar_asset(screen, "start hover", "start hover")

    else:
        gambar_asset(screen, "start", "start")

# ==================================================
# MENAMPILKAN LEVEL SELECTION
# ==================================================

def draw_level_selection(screen, data_game):

    # Menampilkan background Level Selection.
    gambar_background(screen, "bg pilih level")
    # Menampilkan judul Pilih Level.
    gambar_asset(screen, "pilih level", "judul_level")
    # Mengambil level tertinggi yang sudah terbuka
    unlocked_level = data_game.get("unlocked_level", 1)

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

        gambar_asset(screen, nama_asset, f"stage_{level}")

# ==================================================
# MENGGAMBAR TILE
# ==================================================

def draw_tiles(screen, tiles):

    # Menghubungkan jenis tile dengan asset
    asset_tiles = {
        "normal": "blok lantai",
        "bridge": "blok lantai bridge",
        "goal": "blok lantai goal",
        "o": "blok lantai o",
        "x": "blok lantai x"
    }

    # Mengambil konfigurasi papan
    if "board_origin" not in ASSET_LAYOUT:
        return

    origin = ASSET_LAYOUT["board_origin"]["pos"]
    tile_size = TILE_SIZE

    # Menggambar tile berdasarkan koordinat LEVELS
    for koordinat, jenis in tiles.items():

        x, y = koordinat

        posisi = (
            origin[0] + x * tile_size,
            origin[1] + y * tile_size
        )

        nama_asset = asset_tiles.get(jenis)

        if nama_asset not in ASSETS:
            continue

        gambar = pygame.transform.smoothscale(
            ASSETS[nama_asset],
            (tile_size, tile_size)
        )

        screen.blit(gambar, posisi)


# ==================================================
# MENGGAMBAR BLOCK
# ==================================================
def draw_block(screen, state):

    (r1, c1), (r2, c2) = state

    # Mengambil posisi awal papan
    origin = ASSET_LAYOUT["blok lantai"]
    tile_size = TILE_SIZE

    # Block berdiri
    if (r1, c1) == (r2, c2):
        gambar = ASSETS["blok berdiri"]
        ukuran = ASSET_LAYOUT["blok berdiri"]["size"]

    # Block tidur horizontal
    elif r1 == r2:
        gambar = ASSETS["blok tidur"]
        ukuran = ASSET_LAYOUT["blok tidur"]["size"]

    # Block tidur vertikal
    else:
        gambar = pygame.transform.rotate(
            ASSETS["blok tidur"], 90
        )
        ukuran = ASSET_LAYOUT["blok tidur vertikal"]["size"]

    # Menyesuaikan ukuran gambar
    gambar = pygame.transform.smoothscale(gambar, ukuran)

    # Menentukan posisi block berdasarkan koordinat
    x = origin[0] + min(c1, c2) * tile_size
    y = origin[1] + min(r1, r2) * tile_size

    screen.blit(gambar, (x, y))

# ==================================================
# MENAMPILKAN TOMBOL SOLVER
# ==================================================

def draw_solver_buttons(screen, data_game):

    # Mengambil algoritma yang dipilih
    solver_method = data_game.get("solver_method")

    daftar_solver = {
        "BFS": ("bfs idle", "bfs selected"),
        "DFS": ("dfs idle", 
        "dfs selected"),
        "UCS": ("ucs idle", "ucs selected")
    }

    # Menampilkan tombol BFS, DFS, dan UCS
    for nama, asset in daftar_solver.items():

        if solver_method == nama:
            nama_asset = asset[1]

        else:
            nama_asset = asset[0]

        gambar_asset(screen, nama_asset, nama_asset)

    # Menampilkan tombol Solve
    gambar_asset(screen,"solve","solve")


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
# MENAMPILKAN SOLVER ALGORITMA SEARCH
# ==================================================

def draw_solver_performance(screen, data_game):
# Membuat lapisan gelap di belakang pop-up
    overlay = pygame.Surface(
        screen.get_size(),
        pygame.SRCALPHA
    )

    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))

    # Menampilkan panel Solver Performance
    gambar_asset(screen,"solver performance","solver performance")

    # Mengambil hasil pencarian dari solver.py
    hasil = data_game.get("solver_stats", {})

    informasi = [
        ("Algorithm", hasil.get("algorithm", "-")),
        ("Path Length", len(hasil.get("path", []))),
        ("Discovered State", hasil.get("discovered", "-")),
        ("Expanded State", hasil.get("expanded", "-")),
        ("Execution Time", f"{hasil.get('time', 0):.6f} s")
    ]

    # Menampilkan statistik Solver
    for index, (label, nilai) in enumerate(informasi):

        layout_key = f"solver_text_{index}"

        if layout_key not in ASSET_LAYOUT:
            continue

        layout = ASSET_LAYOUT[layout_key]
        posisi = layout["pos"]
        ukuran = layout["size"]

        gambar_teks(
            screen,
            f"{label}: {nilai}",
            posisi,
            ukuran
        )

# ==================================================
# MENAMPILKAN GAMEPLAY
# ==================================================

def draw_gameplay(screen, data_game):

    # Mengambil data level yang sedang dimainkan.
    level = data_game.get("level")
    if level not in LEVELS:
        return

    data_level = LEVELS[level]
    # Menampilkan background sesuai level.
    gambar_background(screen, f"bg lvl {level}")
    # Menggambar tile berdasarkan koordinat.
    draw_tiles(screen, data_level["tiles"])
    # Menggambar goal.
    # Menggambar block sesuai posisi dan orientasi.
    draw_block(screen, data_game.get("posisi_block"))
    # Menampilkan tombol Solve, BFS, DFS, dan UCS.
    draw_solver_buttons(screen, data_game)
    # Menampilkan Puzzle Guide.
    draw_puzzle_guide(screen)
    # Menampilkan Solver Performance
    if data_game.get("solver_show_performance", False):

        draw_solver_performance(screen, data_game)


# ==================================================
# MENAMPILKAN WIN DAN LOSE
# ==================================================

def draw_win(screen):

    # Menampilkan tampilan Congratulations.
    gambar_asset(screen,"menang","win_popup")
    # Menampilkan tombol Next Level.

def draw_jumpscare(screen, data_game):

    # Mengambil level yang sedang dimainkan
    level = data_game.get("level")

    # Menampilkan gambar jumpscare sesuai level
    gambar_background(screen, f"bg js lvl {level}")

# ==================================================
# MENAMPILKAN PARTY
# ==================================================

def draw_party(screen):

    # Menampilkan background Party
    gambar_background(screen,"bg party")

    # Menampilkan lantai Party
    gambar_asset(screen, "lantai party","party_floor")

# ==================================================
# MENAMPILKAN PAGE SESUAI KONDISI GAME
# ==================================================

def draw_page(screen, data_game):
    if not ASSETS:
        load_assets()

    page = data_game["page"]

    if page == "landing":
        draw_landing(screen)

    elif page == "level_select":
        draw_level_selection(screen, data_game)

    elif page == "gameplay":
        draw_gameplay(screen, data_game)

    elif page == "win":
        draw_gameplay(screen, data_game)
        draw_win(screen)

    elif page == "jumpscare":
        draw_jumpscare(screen, data_game)

    elif page == "party":
        draw_party(screen)