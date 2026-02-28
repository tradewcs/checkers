from app.board import Board


def main():
    board = Board()
    board.print_board()
    print()
    board.flip_board()
    board.print_board()


if __name__ == "__main__":
    main()

    chars = ("⬜", "⬛", "○", "◎", "●", "◉", "o", "▪", "▫", "#", "[]")
