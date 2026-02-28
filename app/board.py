from enum import Enum

from app.piece import Piece, Color, PieceType


class Direction(Enum):
    TOP_LEFT = (1, -1)
    TOP_RIGHT = (1, 1)
    BOT_LEFT = (-1, -1)
    BOT_RIGHT = (-1, 1)


class Node:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.value: Piece | None = None
        self.neighbors: dict[Direction, Node] = {}

    def __repr__(self) -> str:
        return f"Node({self.row}, {self.col}, piece={self.value})"

    def __str__(self) -> str:
        return str(self.value)


class Board:
    def __init__(self, width: int = 8, height: int = 8) -> None:
        self.width = width
        self.height = height
        self.board: list[list[Node]] = self.build_board()
        self.is_board_flipped = False
        self.setup_pieces()

    def __getitem__(self, index: int) -> list[Node]:
        return self.board[index]

    def flip_board(self) -> None:
        self.is_board_flipped = not self.is_board_flipped

    def build_board(self) -> list[list[Node]]:
        board = [
            [Node(row, col) for col in range(self.width)]
            for row in range(self.height)
        ]

        for row in range(self.height):
            for col in range(self.width):
                if (row + col) % 2 == 1:
                    continue

                node: Node = board[row][col]
                if row > 0 and col > 0:
                    node.neighbors[Direction.BOT_LEFT] = board[row-1][col-1]
                if row > 0 and col < self.width - 1:
                    node.neighbors[Direction.BOT_RIGHT] = board[row-1][col+1]
                if row < self.height - 1 and col > 0:
                    node.neighbors[Direction.TOP_LEFT] = board[row+1][col-1]
                if row < self.height - 1 and col < self.width - 1:
                    node.neighbors[Direction.TOP_RIGHT] = board[row+1][col+1]

        return board

    def setup_pieces(self) -> None:
        for i in range(self.height):
            for j in range(self.width):
                if (i + j) % 2 != 0:
                    continue

                if i < self.width // 2 - 1:
                    self.board[i][j].value = Piece(
                        Color.WHITE,
                        PieceType.MAN
                    )
                if i >= self.width // 2 + 1:
                    self.board[i][j].value = Piece(
                        Color.BLACK,
                        PieceType.MAN
                    )

    def print_row(self, row: list[Node], end="\n") -> None:
        if not self.is_board_flipped:
            row = reversed(row)

        for node in row:
            if node.value:
                print(node.value, end=" ")
            else:
                if (node.row + node.col) % 2 == 0:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
        print(end=end)

    def print_board(self) -> None:
        board = self.board
        if self.is_board_flipped:
            board = reversed(board)

        for row in board:
            self.print_row(row)
