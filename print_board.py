UNICODE_PIECES = {
    "K": "♔",
    "Q": "♕",
    "R": "♖",
    "B": "♗",
    "N": "♘",
    "P": "♙",
    "k": "♚",
    "q": "♛",
    "r": "♜",
    "b": "♝",
    "n": "♞",
    "p": "♟",
    " ": " ",
}


def print_board(board, unicode=False):
    if unicode:
        for row in board:
            for i, p in row:
                row[i] = UNICODE_PIECES[p]

    print("\n  +---+---+---+---+---+---+---+---+")
    for i, row in enumerate(board):
        rank = 8 - i
        print(f"{rank} | " + " | ".join(row) + " |")
        print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h\n")
