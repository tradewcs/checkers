from app.board import Board
from app.move import Move
from app.piece import PieceType


class CheckersEngine:
    def __init__(self, board: Board) -> None:
        self.board = board or Board()

    def _get_capture_move(self, from_position: tuple[int, int]):
        ...

    def allowed_directions(self) -> set:
        ...

    def get_man_moves(self) -> list[Move]:
        valid_moves = []

        for row in self.board:
            for node in row:
                if not node.value or node.value.piece_type is not PieceType.MAN:
                    continue

                for direction, neighbour in node.neighbors.items():
                    if neighbour.value is None and :
                        valid_moves.append(
                            Move(
                                (node.row, node.col),
                                (neighbour.row, neighbour.col),
                                captured=[],
                                next=None
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
