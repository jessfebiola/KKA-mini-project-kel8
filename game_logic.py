# ==================================================
# MENGATUR GERAKAN BLOCK - MEMBER 3
# Koordinat state: ((x1,y1),(x2,y2))
# ==================================================

def move_block(state, direction):
    (x1, y1), (x2, y2) = state
    if (x1, y1) == (x2, y2):
        if direction == "UP":
            return ((x1, y1 - 2), (x1, y1 - 1))
        elif direction == "DOWN":
            return ((x1, y1 + 1), (x1, y1 + 2))
        elif direction == "LEFT":
            return ((x1 - 2, y1), (x1 - 1, y1))
        elif direction == "RIGHT":
            return ((x1 + 1, y1), (x1 + 2, y1))
    elif y1 == y2:
        left = min(x1, x2)
        right = max(x1, x2)
        if direction == "UP":
            return ((left, y1 - 1), (right, y1 - 1))
        elif direction == "DOWN":
            return ((left, y1 + 1), (right, y1 + 1))
        elif direction == "LEFT":
            return ((left - 1, y1), (left - 1, y1))
        elif direction == "RIGHT":
            return ((right + 1, y1), (right + 1, y1))
    elif x1 == x2:
        top = min(y1, y2)
        bottom = max(y1, y2)
        if direction == "LEFT":
            return ((x1 - 1, top), (x1 - 1, bottom))
        elif direction == "RIGHT":
            return ((x1 + 1, top), (x1 + 1, bottom))
        elif direction == "UP":
            return ((x1, top - 1), (x1, top - 1))
        elif direction == "DOWN":
            return ((x1, bottom + 1), (x1, bottom + 1))
    raise ValueError("Arah gerakan tidak valid")

def check_fall(state, tiles):
    return any(posisi not in tiles for posisi in state)

def check_win(state, goal):
    return state[0] == state[1] == goal

def update_bridges(state, tiles, bridge_o_open=False, bridge_x_open=False):
    # O dapat diaktifkan ketika balok berdiri ataupun tidur.
    if any(tiles.get(posisi) == "o" for posisi in state):
        bridge_o_open = True
    # X hanya aktif ketika balok berdiri.
    if state[0] == state[1] and tiles.get(state[0]) == "x":
        bridge_x_open = True
    return bridge_o_open, bridge_x_open
