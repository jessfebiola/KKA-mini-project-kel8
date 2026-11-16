## Anggota Kelompok

| No           | Name        | NRP     |
| ---            | ---        | ----------|
|  |  |  |
| 1 | Luthfir Rizqy Fathullah Hanggi | 5025251081 |
| 2 | Yesenia Valencia W| 5025251182 | 
| 3 | Claresta Amelinda H. | 5025251184 | 
| 4 | Jessica Febiola| 5025251216 | 
| 5 | I Made Bagus Naratama | 5025251233 | 

# Roll to Vivat

Roll to Vivat adalah game puzzle berbasis Python dan Pygame yang terinspirasi dari permainan Bloxorz. Pemain menggerakkan sebuah balok di atas papan untuk mencapai kotak tujuan tanpa terjatuh dari jalur. Game ini menyediakan tiga level dengan tantangan yang berbeda serta fitur Solver untuk mencari urutan gerakan secara otomatis.

## Fitur

- **3 level permainan** dengan susunan papan dan tantangan yang berbeda.
- **Kontrol manual** menggunakan tombol panah pada keyboard.
- **Mekanisme jembatan di Level 2** yang melibatkan switch O dan X.
- **Solver otomatis** menggunakan tiga algoritma pencarian:
  - **BFS (Breadth-First Search):** menelusuri kemungkinan gerakan berdasarkan urutan tingkat kedalaman.
  - **DFS (Depth-First Search):** menelusuri satu jalur lebih dalam sebelum mencoba jalur lain.
  - **UCS (Uniform-Cost Search):** memilih state berdasarkan total biaya gerakan.
- **Solver Performance** untuk menampilkan jumlah state yang ditemukan, jumlah state yang diperiksa, dan waktu pencarian.
- **Musik latar dan efek suara** untuk halaman permainan, halaman party, serta jumpscare.
- **Tampilan yang dapat menyesuaikan ukuran jendela** tanpa mengubah proporsi desain permainan.

## Teknologi

- Python
- Pygame

## Struktur Proyek

```text
KKA-mini-project-kel8/
├── assets/
│   ├── bgsound/
│   └── ... (gambar dan aset permainan lainnya)
├── vivatfortc/
│   ├── dfs_vivatfortc.py
│   └── testmap_vivatfortc.py
├── fireworks.py
├── game_logic.py
├── game_render.py
├── main.py
└── solver.py
```

### Fungsi File Utama

| File | Keterangan |
|---|---|
| `main.py` | Menjalankan game, mengatur navigasi halaman, input pemain, sound, dan proses Solver. |
| `game_logic.py` | Mengatur pergerakan balok, pengecekan balok jatuh atau mencapai tujuan, serta aktivasi jembatan. |
| `game_render.py` | Mengatur data level, pemuatan aset, layout, dan tampilan setiap halaman permainan. |
| `solver.py` | Berisi implementasi algoritma BFS, DFS, dan UCS. |
| `fireworks.py` | Mengatur efek kembang api pada bagian akhir permainan. |
| `assets/` | Menyimpan gambar, background, dan musik yang digunakan dalam game. |
| `vivatfortc/` | Menyimpan file Python pendukung yang terdapat dalam proyek. |

## Persiapan dan Instalasi

Pastikan Python sudah terpasang di komputer.

1. Clone repository:

   ```bash
   git clone <URL-REPOSITORY>
   ```

2. Masuk ke folder proyek:

   ```bash
   cd KKA-mini-project-kel8
   ```

3. Install Pygame:

   ```bash
   pip install pygame
   ```

## Cara Menjalankan Game

Jalankan perintah berikut dari folder utama proyek:

```bash
python main.py
```

Pastikan folder `assets/` tetap berada di dalam folder proyek agar gambar dan musik dapat dimuat dengan benar.

## Kontrol Permainan

| Tombol / Input | Fungsi |
|---|---|
| `↑` | Menggerakkan balok ke atas |
| `↓` | Menggerakkan balok ke bawah |
| `←` | Menggerakkan balok ke kiri |
| `→` | Menggerakkan balok ke kanan |
| `R` | Mengulang level yang sedang dimainkan |
| `ESC` | Kembali ke halaman sebelumnya atau menu pemilihan level |
| `ENTER` | Melanjutkan dari halaman kemenangan |
| Klik **BFS / DFS / UCS** | Memilih algoritma Solver |
| Klik **Solve** | Menjalankan Solver yang dipilih |

## Cara Menggunakan Solver

1. Masuk ke salah satu level.
2. Pilih algoritma **BFS**, **DFS**, atau **UCS** pada bagian Solver.
3. Klik tombol **Solve**.
4. Solver akan mencari urutan gerakan menuju kotak tujuan.
5. Jika solusi ditemukan, balok akan bergerak otomatis mengikuti hasil pencarian.
6. Setelah proses selesai, informasi performa Solver akan ditampilkan.

## Catatan

- Setiap gerakan pemain maupun Solver mengikuti aturan posisi balok pada permainan Bloxorz.
- Balok harus tetap berada di atas tile yang tersedia. Jika keluar dari jalur, permainan akan masuk ke halaman jumpscare.
- Level 2 memiliki mekanisme switch untuk mengaktifkan jembatan.
- Untuk menjalankan game, gunakan folder proyek secara utuh dan jangan memisahkan file Python dari folder `assets/`.

## 📸 Dokumentasi
### 1. Landing Page

<img width="1388" height="988" alt="image" src="https://github.com/user-attachments/assets/b5217b91-2a53-4228-8913-428cae9d542f" />

*Tampilan awal Roll to Vivat dengan tombol Start.*

### 2. Pemilihan Level

<img width="1381" height="982" alt="image" src="https://github.com/user-attachments/assets/ab2eb3c7-5970-48a1-80d9-52191db47a5a" />

*Tampilan pemilihan tiga stage dengan sistem unlock.*

### 3. Gameplay Level 1

<img width="1371" height="986" alt="image" src="https://github.com/user-attachments/assets/ac667f66-5d82-432a-9c7a-b47235088841" />


*Pemain mengarahkan balok menuju petak tujuan.*

### 4. Gameplay Level 2

<img width="1371" height="986" alt="image" src="https://github.com/user-attachments/assets/b49765b7-8be3-4328-9722-473f37dd65aa" />

*Tantangan tombol O dan X untuk membuka jembatan.*

### 5. Gameplay Level 3

<img width="1371" height="986" alt="image" src="https://github.com/user-attachments/assets/7271ee5e-d858-40bc-b471-e50436936f72" />


*Tantangan lintasan pada level terakhir.*

### 6. Solver dan Statistik

<img width="1371" height="986" alt="image" src="https://github.com/user-attachments/assets/b86c9691-6b37-4c69-a326-79ea5e663be6" />


*Pilihan Algoritma solver dan statistik hasil pencarian.*

### 7. Ending / Party

<img width="1371" height="986" alt="image" src="https://github.com/user-attachments/assets/e9eb016a-212c-497d-9c11-2e39d04d1964" />


*Tampilan akhir setelah pemain menyelesaikan permainan.*

## Daftar Pustaka

Clarke, D. (1999). Bloxorg [Video Game].https://www.coolmathgames.com/0-bloxorz?variant=next
Iyer. S. (2012). Bloxorg. Github. https://github.com/supersaiyanmode/Bloxorz
