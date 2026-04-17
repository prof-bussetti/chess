def valid_pawn_move(
    col_start: int, row_start: int, col_end: int, row_end: int, board: list[list]
):
    """Checks if the move is valid for a pawn on this board,
    moving from start to end coordinates"""

    # Flip the board
    board = board[::-1]

    # Understand pawn side and double check piece
    piece_start = board[row_start][col_start]
    assert piece_start.lower() == "p"

    forward_direction = 1
    if piece_start == "p":
        forward_direction = -1

    # initialize empty legal moves list
    legal_moves = []

    # --------- Add legal moves one by one ------------------

    # MOVE: one step forward & two steps forward

    # Check that we are still in the board
    if 0 <= row_start + forward_direction <= 7:

        # Check if the landing square is empty
        if board[row_start + forward_direction][col_start] == " ":
            legal_moves.append((forward_direction, 0))

            # Già che ci siamo, controlliamo anche il doppio passo
            starting_pawn_row = 1 if forward_direction == 1 else 6
            if row_start == starting_pawn_row:
                if board[row_start + 2 * forward_direction][col_start] == " ":
                    legal_moves.append((2 * forward_direction, 0))

    # MOVE: diagonal captures

    # Check both right and left captures
    for c_delta in (1, -1):

        # Check that we are still in the board
        if 0 <= row_start + forward_direction <= 7 and 0 <= col_start + c_delta <= 7:

            ending_square = board[row_start + forward_direction][col_start + c_delta]

            if ending_square in "rnbqp" and piece_start.isupper():
                legal_moves.append((forward_direction, c_delta))

            if ending_square in "RNBQP" and piece_start.islower():
                legal_moves.append((forward_direction, c_delta))

    return (row_end - row_start, col_end - col_start) in legal_moves
