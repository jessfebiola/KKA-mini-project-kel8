# ==================================================
# MENGATUR GERAKAN BLOCK
# MEMBER 3
# ==================================================

def move_block(state, direction):

    (r1, c1), (r2, c2) = state

    # Block berdiri
    if (r1, c1) == (r2, c2):

        if direction == "UP":
            return ((r1 - 2, c1), (r1 - 1, c1))
        elif direction == "DOWN":
            return ((r1 + 1, c1), (r1 + 2, c1))
        elif direction == "LEFT":
            return ((r1, c1 - 2), (r1, c1 - 1))
        elif direction == "RIGHT":
            return ((r1, c1 + 1), (r1, c1 + 2))

    # Block tidur horizontal
    elif r1 == r2:
        left = min(c1, c2)
        right = max(c1, c2)

        if direction == "UP":
            return ((r1 - 1, left), (r1 - 1, right))
        elif direction == "DOWN":
            return ((r1 + 1, left), (r1 + 1, right))
        elif direction == "LEFT":
            return ((r1, left - 1), (r1, left - 1))
        elif direction == "RIGHT":
            return ((r1, right + 1), (r1, right + 1))

    # Block tidur vertikal
    elif c1 == c2:
        top = min(r1, r2)
        bottom = max(r1, r2)

        if direction == "LEFT":
            return ((top, c1 - 1), (bottom, c1 - 1))
        elif direction == "RIGHT":
            return ((top, c1 + 1), (bottom, c1 + 1))
        elif direction == "UP":
            return ((top - 1, c1), (top - 1, c1))
        elif direction == "DOWN":
            return ((bottom + 1, c1), (bottom + 1, c1))

    raise ValueError("Arah gerakan tidak valid")


# ==================================================
# MENGECEK BLOCK JATUH
# ==================================================

def check_fall(state, tiles):

    return any(posisi not in tiles for posisi in state)


# ==================================================
# MENGECEK KONDISI MENANG
# ==================================================

def check_win(state, goal):

    return state[0] == state[1] == goal
