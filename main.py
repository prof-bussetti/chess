fen_start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"


def fen2matrix(fen):
    def row2list(row):
        l = []

        for c in row:
            if c.isdigit():
                l += [" "] * int(c)
            else:
                l.append(c)

        return l

    board = []

    for row in fen.split("/"):
        board.append(row2list(row))

    return board


def matrix2fen(board):
    def row2str(row):
        f = ""
        spaces = 0

        for c in row:
            if c == " ":
                spaces += 1
            else:
                if spaces > 0:
                    f += str(spaces)
                    spaces = 0
                f += c

        if spaces > 0:
            f += str(spaces)
            spaces = 0

        return f

    fen = ""
    for row in board:
        fen += row2str(row) + "/"

    return fen[:-1]
