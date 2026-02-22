from enum import Enum

from piece import Piece, Color, PieceType


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
        return f"Node({self.row}, {self.col}, piece={self.piece})"


class Board:
    def __init__(self, width: int = 8, height: int = 8) -> None:
        self.width = width
        self.height = height
        self.board: list[list[Node]] = self.build_board()

    def build_board(self) -> list[list[Node]]:
        board = [
            [Node(row, col) for col in range(self.width)]
            for row in range(self.height)
        ]

        for row in range(self.height):
            for col in range(self.width):
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

    def print_board(self) -> None:
        for row in self.board:
            out = []
            for node in row:
                piece = node.value
                if piece is None:
                    out.append(".")
                else:
                    char = "w" if piece.color == Color.WHITE else "b"
                    if piece.piece_type == PieceType.KING:
                        char = char.upper()
                    out.append(char)
            print(" ".join(out))
