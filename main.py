import pygame

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

    # Data Solver
    "solver_method": None,      # Algoritma yang dipilih: BFS, DFS, UCS
    "solver_result": [],        # Hasil urutan gerakan Solver
    "solver_index": 0,          # Urutan gerakan yang sedang dijalankan
    "solver_running": False,    # Status Solver
    "solver_last_time": 0       # Waktu gerakan Solver terakhir
}


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

    # Mendeteksi tombol arah keyboard.
    # Menentukan arah: UP, DOWN, LEFT, atau RIGHT.
    # Memanggil move_block() dari game_logic.py.
    # Memperbarui posisi block.
    # Memastikan gerakan tidak dilakukan ketika Solver berjalan.

    pass


def cek_game():

    # Memanggil check_fall() dari game_logic.py
    # untuk mengecek apakah block jatuh.

    # Jika block jatuh:
    # status = "lose"
    # page = "lose"

    # Memanggil check_win() dari game_logic.py
    # untuk mengecek apakah block mencapai goal.

    # Jika block mencapai goal:
    # status = "win"
    # page = "win"

    pass


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

    # D. MENAMPILKAN PAGE
    # Memanggil draw_page() dari game_render.py
    draw_page(screen, data_game)

    # E. MEMPERBARUI TAMPILAN
    pygame.display.flip()

    # Membatasi game menjadi 60 FPS
    clock.tick(60)


# Menutup Pygame
pygame.quit()
