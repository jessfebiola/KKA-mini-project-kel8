# Mengambil aturan pergerakan dan pengecekan game
# dari game_logic.py.
import heapq
import time
from collections import deque

from game_logic import move_block, check_fall, check_win


# Urutan arah yang dicoba oleh semua algoritma.
DIRECTIONS = ("UP", "DOWN", "LEFT", "RIGHT")


# ==================================================
# FUNGSI BANTU
# ==================================================

def normalize(state):
    # Menyamakan urutan dua sel block supaya state yang sama
    # selalu punya bentuk yang sama (penting untuk visited).
    a, b = state
    return (a, b) if a <= b else (b, a)


def move_cost(state, new_state):
    return 1


def successors(state, level_data):
    # Menghasilkan (arah, state_baru) untuk gerakan yang tidak membuat
    # block jatuh. State yang jatuh langsung dibuang.
    tiles = level_data["tiles"]

    for direction in DIRECTIONS:
        new_state = normalize(move_block(state, direction))

        if check_fall(new_state, tiles):
            continue

        yield direction, new_state


def build_path(parent, state):
    # Menyusun urutan gerakan dari start ke state dengan
    # menelusuri parent mundur.
    path = []

    while parent[state] is not None:
        state, direction = parent[state]
        path.append(direction)

    path.reverse()
    return path


def make_result(algorithm, path, discovered, expanded, start_time):
    return {
        "algorithm": algorithm,
        "path": path,
        "discovered": discovered,
        "expanded": expanded,
        "time": time.perf_counter() - start_time,
    }


# ==================================================
# BREADTH FIRST SEARCH (BFS)
# ==================================================

def bfs(start_state, level_data):

    # Menggunakan Queue untuk menyimpan state yang akan diperiksa.
    # Memulai pencarian dari posisi awal block.
    # Memeriksa kemungkinan gerakan ke empat arah.
    # Menghindari state yang sudah pernah dikunjungi.
    # Menghentikan pencarian jika goal ditemukan.
    # Mengembalikan urutan gerakan menuju goal.

    start_time = time.perf_counter()
    goal = level_data["goal"]

    start = normalize(start_state)

    # parent[state] = (state_sebelumnya, arah) atau None untuk start
    parent = {start: None}
    queue = deque([start])
    expanded = 0

    if check_win(start, goal):
        return make_result("BFS", [], len(parent), expanded, start_time)

    while queue:
        state = queue.popleft()
        expanded += 1

        for direction, new_state in successors(state, level_data):

            if new_state in parent:
                continue

            parent[new_state] = (state, direction)

            # BFS menemukan goal pertama dengan gerakan paling sedikit.
            if check_win(new_state, goal):
                path = build_path(parent, new_state)
                return make_result("BFS", path, len(parent),
                                   expanded, start_time)

            queue.append(new_state)

    # Tidak ada solusi
    return make_result("BFS", [], len(parent), expanded, start_time)


# ==================================================
# DEPTH FIRST SEARCH (DFS)
# ==================================================

def dfs(start_state, level_data):

    # Menggunakan Stack untuk menyimpan state yang akan diperiksa.
    # Memulai pencarian dari posisi awal block.
    # Memeriksa kemungkinan gerakan ke empat arah.
    # Menghindari state yang sudah pernah dikunjungi.
    # Menghentikan pencarian jika goal ditemukan.
    # Mengembalikan urutan gerakan menuju goal.

    start_time = time.perf_counter()
    goal = level_data["goal"]

    start = normalize(start_state)

    parent = {start: None}
    stack = [start]
    expanded = 0

    if check_win(start, goal):
        return make_result("DFS", [], len(parent), expanded, start_time)

    while stack:
        state = stack.pop()
        expanded += 1

        if check_win(state, goal):
            path = build_path(parent, state)
            return make_result("DFS", path, len(parent),
                               expanded, start_time)

        # Dibalik supaya arah pertama di DIRECTIONS dicoba lebih dulu
        # (stack mengambil elemen terakhir yang dimasukkan).
        for direction, new_state in reversed(list(
                successors(state, level_data))):

            if new_state in parent:
                continue

            parent[new_state] = (state, direction)
            stack.append(new_state)

    # Tidak ada solusi
    return make_result("DFS", [], len(parent), expanded, start_time)


# ==================================================
# UNIFORM COST SEARCH (UCS)
# MEMBER 4
# ==================================================

def ucs(start_state, level_data):

    # Menggunakan Priority Queue untuk menyimpan state.
    # Memberikan biaya pada setiap gerakan.
    # Memulai pencarian dari posisi awal block.
    # Memeriksa kemungkinan gerakan ke empat arah.
    # Menghindari state yang sudah pernah dikunjungi
    # dengan biaya yang lebih baik.
    # Menghentikan pencarian jika goal ditemukan.
    # Mengembalikan urutan gerakan menuju goal.

    start_time = time.perf_counter()
    goal = level_data["goal"]

    start = normalize(start_state)

    parent = {start: None}
    best_cost = {start: 0}

    # Isi heap: (biaya, nomor urut, state). Nomor urut menjaga
    # urutan stabil kalau ada biaya yang sama.
    counter = 0
    heap = [(0, counter, start)]
    closed = set()
    expanded = 0

    while heap:
        cost, _, state = heapq.heappop(heap)

        # Lewati entri usang (state sudah ditemukan dengan biaya lebih baik).
        if state in closed:
            continue
        closed.add(state)
        expanded += 1

        # Goal dicek saat diambil dari heap, bukan saat ditemukan, agar cost paling kecil.
        if check_win(state, goal):
            path = build_path(parent, state)
            result = make_result("UCS", path, len(best_cost),
                                 expanded, start_time)
            result["cost"] = cost
            return result

        for direction, new_state in successors(state, level_data):

            new_cost = cost + move_cost(state, new_state)

            if new_state in best_cost and new_cost >= best_cost[new_state]:
                continue

            best_cost[new_state] = new_cost
            parent[new_state] = (state, direction)

            counter += 1
            heapq.heappush(heap, (new_cost, counter, new_state))

    # Tidak ada solusi
    return make_result("UCS", [], len(best_cost), expanded, start_time)


