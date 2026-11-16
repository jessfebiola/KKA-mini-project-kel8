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

pass


# ==================================================
# MENGATUR POSISI DAN UKURAN ASSET
# MEMBER 2
# ==================================================

# Mengatur posisi dan ukuran background.
# Mengatur posisi tombol Start, Setting, dan Credit.
# Mengatur posisi tombol Solve, BFS, DFS, dan UCS.
# Mengatur posisi Puzzle Guide.
# Mengatur posisi Solver Performance.
# Mengatur ukuran dan posisi tile, block, serta goal.

pass


# ==================================================
# MENAMPILKAN LANDING
# ==================================================

def draw_landing(screen):

    # Menampilkan background Landing.
    # Menampilkan logo game.

    pass


# ==================================================
# MENAMPILKAN LEVEL SELECTION
# ==================================================

def draw_level_selection(screen):

    # Menampilkan background Level Selection.
    # Menampilkan judul Pilih Level.
    # Menampilkan pilihan Stage 1, Stage 2, dan Stage 3.
    # Menampilkan icon level terkunci atau terbuka.

    pass


# ==================================================
# MENAMPILKAN GAMEPLAY
# ==================================================

def draw_gameplay(screen, data_game):

    # Mengambil data level yang sedang dimainkan.
    # Menampilkan background sesuai level.
    # Menggambar tile berdasarkan koordinat.
    # Menggambar goal.
    # Menggambar block sesuai posisi dan orientasi.
    # Menampilkan tombol Solve, BFS, DFS, dan UCS.
    # Menampilkan Puzzle Guide.
    # Menampilkan Solver Performance jika diperlukan.

    pass


# ==================================================
# MENAMPILKAN WIN DAN LOSE
# ==================================================

def draw_win(screen):

    # Menampilkan tampilan Congratulations.
    # Menampilkan tombol Next Level.

    pass


def draw_lose(screen):

    # Menampilkan tampilan You Didn't Make It.
    # Menampilkan tombol Retry.

    pass

# ==================================================
# MENAMPILKAN PARTY
# ==================================================

def draw_party(screen):

    # Menampilkan background Party.
    # Menampilkan lantai Party.
    # Menampilkan elemen tambahan jika diperlukan.

    screen.blit(ASSETS["bg party"], (0, 0))
    screen.blit(ASSETS["lantai party"], (0, 0))

# ==================================================
# MENAMPILKAN PAGE SESUAI KONDISI GAME
# ==================================================

def draw_page(screen, data_game):

    page = data_game["page"]

    if page == "landing":
        draw_landing(screen)

    elif page == "level_select":
        draw_level_selection(screen)

    elif page == "gameplay":
        draw_gameplay(screen, data_game)

    elif page == "win":
        draw_win(screen)

    elif page == "lose":
        draw_lose(screen)

    elif page == "party":
        draw_party(screen)