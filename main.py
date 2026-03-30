from utils import fen2matrix, FEN_START
from print_board import print_board

board = fen2matrix(FEN_START)

while True:
    print_board(board)
    move = input("\nPlay your move\n\n>> ")
