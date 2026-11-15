import pygame


# ==================================================
# DATA LEVEL
# ==================================================

# Menyimpan susunan tile, posisi awal block,
# dan posisi goal setiap level.

LEVELS = {

    1: {
        "tiles": [
            # Isi koordinat tile Level 1.
        ],

        "start": None,  # Isi posisi awal block.
        "goal": None    # Isi posisi goal.
    },

    2: {
        "tiles": [
            # Isi koordinat tile Level 2.
        ],

        "start": None,
        "goal": None
    },

    3: {
        "tiles": [
            # Isi koordinat tile Level 3.
        ],

        "start": None,
        "goal": None
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
    # Menampilkan tombol Start, Setting, dan Credit.

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