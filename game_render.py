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
# MENAMPILKAN SETTING DAN CREDIT
# ==================================================

def draw_setting(screen):

    # Menampilkan halaman Setting.

    pass


def draw_credit(screen):

    # Menampilkan halaman Credit.

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

    elif page == "setting":
        draw_setting(screen)

    elif page == "credit":
        draw_credit(screen)
