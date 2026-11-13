
# dfs.py

def get_block_tiles(state):
    x, y, orientation = state

    if orientation == "S":
        return [(x, y)]

    elif orientation == "H":
        return [(x, y), (x + 1, y)]

    elif orientation == "V":
        return [(x, y), (x, y + 1)]

    
def is_valid(state, map_data):
    tiles = get_block_tiles(state)

    height = len(map_data)
    width = len(map_data[0])

    for x, y in tiles:

        # Memeriksa batas map
        if x < 0 or x >= width or y < 0 or y >= height:
            return False

        # Memeriksa apakah tile bisa dilewati
        if map_data[y][x] == "#":
            return False

    return True

def get_next_states(state):
    x, y, orientation = state

    next_states = []

    if orientation == "S":
        next_states = [
            (x - 2, y, "H"),  # Kiri
            (x + 1, y, "H"),  # Kanan
            (x, y - 2, "V"),  # Atas
            (x, y + 1, "V")   # Bawah
        ]

    elif orientation == "H":
        next_states = [
            (x - 1, y, "S"),  # Kiri
            (x + 2, y, "S"),  # Kanan
            (x, y - 1, "H"),  # Atas
            (x, y + 1, "H")   # Bawah
        ]

    elif orientation == "V":
        next_states = [
            (x - 1, y, "V"),  # Kiri
            (x + 1, y, "V"),  # Kanan
            (x, y - 1, "S"),  # Atas
            (x, y + 2, "S")   # Bawah
        ]

    return next_states


def get_valid_next_states(state, map_data):
    next_states = get_next_states(state)

    valid_states = []

    for next_state in next_states:
        if is_valid(next_state, map_data):
            valid_states.append(next_state)

    return valid_states



def find_start_goal(map_data):
    start = None
    goal = None

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):

            if tile == "S":
                start = (x, y, "S")

            elif tile == "G":
                goal = (x, y)

    return start, goal


def reconstruct_path(parent, goal_state):
    path = []
    current = goal_state

    while parent[current] is not None:
        previous_state, move = parent[current]

        path.append(move)
        current = previous_state

    path.reverse()

    return path


def dfs(map_data):
    start, goal = find_start_goal(map_data)

    if start is None or goal is None:
        return None, 0

    # Posisi balok harus valid
    if not is_valid(start, map_data):
        return None, 0

    # Stack untuk DFS
    stack = [start]

    # Menyimpan state yang sudah dikunjungi
    visited = {start}

    # Menyimpan asal setiap state
    parent = {start: None}

    # Urutan gerakan sesuai get_next_states()
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    while stack:

        # Mengambil state paling atas dari stack
        current = stack.pop()

        # Memeriksa apakah goal sudah tercapai
        if current == (goal[0], goal[1], "S"):
            path = reconstruct_path(parent, current)
            return path, len(visited)

        # Menghasilkan kemungkinan gerakan
        next_states = get_next_states(current)

        # Memeriksa setiap kemungkinan gerakan
        for next_state, move in reversed(
            list(zip(next_states, moves))
        ):

            # Memastikan posisi baru valid
            if is_valid(next_state, map_data):

                # Menghindari state yang sudah dikunjungi
                if next_state not in visited:

                    visited.add(next_state)

                    parent[next_state] = (current, move)

                    stack.append(next_state)

    # Goal tidak ditemukan
    return None, len(visited)

if __name__ == "__main__":

    test_map = [
        "########",
        "#......#",
        "#.S....#",
        "#......#",
        "#......#",
        "#....G.#",
        "########"
    ]

    path, visited_count = dfs(test_map)

    if path is not None:
        print("Goal ditemukan!")
        print("Urutan gerakan:", path)
    else:
        print("Goal tidak ditemukan.")

    print("Jumlah state dikunjungi:", visited_count)