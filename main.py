from app import Board
from app import CheckersEngine


def main():
    board = Board()
    board.print_board()
    print()

    engine = CheckersEngine(board)
    valid_moves = engine.get_valid_man_moves()
    [print(m) for m in valid_moves]

if __name__ == "__main__":
    main()

    chars = ("⬜", "⬛", "○", "◎", "●", "◉", "o", "▪", "▫", "#", "[]")
