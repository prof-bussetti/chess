def valid_rook_move(
    col_start: int, row_start: int, col_end: int, row_end: int, board: list[list]
):
    """Checks if the move is valid for a rook on this board,
    moving from start to end coordinates"""

    board = board[::-1]

    starting_piece = board[row_start][col_start]
    enemy = "QRBPNK" if starting_piece.islower() else "qrbpnk"

    legal_moves = []

    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        for steps in range(1, 8):

            dr, dc = steps * dir[0], steps * dir[1]

            landing_row = row_start + dr
            landing_col = col_start + dc

            landing_square = board[landing_row][landing_col]

            if not (0 <= landing_row <= 7 and 0 <= landing_col <= 7):
                break

            if landing_square == " ":
                legal_moves.append((dr, dc))

            elif landing_square in enemy:
                legal_moves.append((dr, dc))
                break

            else:
                break

    return (row_end - row_start, col_end - col_start) in legal_moves
