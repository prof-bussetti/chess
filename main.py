import json
from utils import show_board

with open("board.json", "r") as f:
    board = json.loads(f.read())

col = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

while True:
    # 1. show board
    show_board(board)

    # 2. get user input move
    move = input("\nPlay your move!\n\n>>> ")

    if move.lower() == "q":
        break

    # 2.1 parse user input (dividere un input in sottoclassi)
    move_start, move_end = move[:2], move[2:]

    col_start = int(col.get(move_start[0]))
    row_start = (
        int(move_start[-1]) - 1
    )  ### indice è indietro di uno rispetto alla coordinata perchè parte da 0

    col_end = int(col.get(move_end[0]))
    row_end = int(move_end[-1]) - 1

    move_start = board[::-1][row_start][col_start]
    move_end = board[::-1][row_end][col_end]
