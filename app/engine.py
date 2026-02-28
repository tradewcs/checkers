from app.board import Board
from app.move import Move


class CheckersEngine:
    def __init__(self, board: Board) -> None:
        if not board:
            self.board = Board()

        self.board = board

    def get_valid_moves(self) -> list[Move]:
        valid_moves = []

        for row in self.board:
            for node in row:
                if not node.value:
                    continue

                for direction, neighbour in node.neighbors.items():
                    if neighbour.value is None:
                        valid_moves.append(
                            Move(
                                (node.row, node.col),
                                (neighbour.row, neighbour.col)
                            )
                        )
                    if node.value.color == neighbour.color:
                        continue

                    vacant_square = neighbour.neighbors.get(direction)
                    if vacant_square and vacant_square.value is None:
                        valid_moves.append(
                            Move(
                                (node.row, node.col),
                                (vacant_square.row, vacant_square.col),
                                [neighbour]
                            )
                        )
