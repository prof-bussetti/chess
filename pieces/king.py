def valid_queen_move(
    col_start: int, row_start: int, col_end: int, row_end: int, board: list[list]
):
    """Checks if the move is valid for a queen on this board,
    moving from start to end coordinates"""

    board = board[::-1]

    starting_piece = board[row_start][col_start]
    enemy = "QRBPNK" if starting_piece.islower() else "qrbpnk"

    legal_moves = []

    for dir in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]:

        dr, dc = dir

        landing_row = row_start + dr
        landing_col = col_start + dc

        if not (0 <= landing_row <= 7 and 0 <= landing_col <= 7):
            continue

        landing_square = board[landing_row][landing_col]

        if landing_square == " ":
            legal_moves.append((dr, dc))

        elif landing_square in enemy:
            legal_moves.append((dr, dc))

    return (row_end - row_start, col_end - col_start) in legal_moves
