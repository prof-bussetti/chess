def valid_queen_move(
    col_start: int, row_start: int, col_end: int, row_end: int, board: list[list]
):
    """Checks if the move is valid for a queen on this board,
    moving from start to end coordinates"""

    # Flip the board
    board = board[::-1]

    # Understand pawn side and double check piece
    piece_start = board[row_start][col_start]
    assert piece_start.lower() == "q"

    # initialize empty legal moves list
    legal_moves = []

    # --------- Add legal moves one by one ------------------

    # MOVE: one step forward & two steps forward

    # Chose a direction
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:

        # Move away from the starting square, at most 7 steps
        for steps in range(1, 8):

            endr, endc = row_start + y * steps, col_start + x * steps
            ending_square = board[endr][endc]

            # Check if it's in the board
            if not (0 <= endr <= 7 and 0 <= endc <= 7):
                break

            # Check if it's an empty square
            if ending_square == " ":
                legal_moves.append((y * steps, x * steps))

            # Check if it's an enemy piece (pt. 1)
            elif ending_square in "rnbqp" and piece_start.isupper():
                legal_moves.append((y * steps, x * steps))
                break

            # Check if it's an enemy piece (pt. 2)
            elif ending_square in "RNBQP" and piece_start.islower():
                legal_moves.append((y * steps, x * steps))
                break

            # Otherwise, it's a friendly piece: stop going in this direction
            else:
                break

    return (row_end - row_start, col_end - col_start) in legal_moves
