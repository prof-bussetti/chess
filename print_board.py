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

# ANSI color codes
LIGHT_SQ = "\033[48;2;240;217;181m"
DARK_SQ = "\033[48;2;181;136;99m"
WHITE_PC = "\033[38;2;255;255;255m"
BLACK_PC = "\033[38;2;0;0;0m"
RESET = "\033[0m"
BOLD = "\033[1m"


def _square_bg(i, j):
    is_light = (i + j) % 2 == 0
    return LIGHT_SQ if is_light else DARK_SQ


def _print_colored(board, unicode):
    print()
    for i, row in enumerate(board):
        line = f" {8 - i} "
        for j, piece in enumerate(row):
            bg = _square_bg(i, j)
            fg = WHITE_PC if piece.isupper() else BLACK_PC
            symbol = UNICODE_PIECES.get(piece, piece) if unicode else piece
            line += f"{bg}{fg}{BOLD} {symbol} {RESET}"
        print(line)
    print()
    print("   " + "".join(c.center(3) for c in "abcdefgh"))
    print()


def _print_simple(board):
    print("  +---+---+---+---+---+---+---+---+")
    for i, row in enumerate(board):
        rank = 8 - i
        print(f"{rank} | " + " | ".join(row) + " |")
        print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h")
    print()


def print_board(board, unicode=True, colored=True):
    if colored:
        _print_colored(board, unicode)
    else:
        _print_simple(board)
