from app import (
    Board,
    Piece,
    Move,
    PieceType,
    PieceColor,
    MoveDirection
)


class CheckersEngine:
    def __init__(self, board: Board) -> None:
        self.board = board or Board()

    def _get_capture_move(
        self,
        piece: Piece,
        from_position: tuple[int, int]
    ) -> Move | None:
        ...

    def allowed_directions(self, color: PieceColor) -> set[MoveDirection]:
        if color is PieceColor.WHITE:
            return {MoveDirection.TOP_RIGHT, MoveDirection.TOP_LEFT}
        if color is PieceColor.BLACK:
            return {MoveDirection.BOT_RIGHT, MoveDirection.BOT_LEFT}

    def get_man_moves(self) -> list[Move]:
        valid_moves = []

        for row in self.board:
            for node in row:
                if not node.value or node.value.piece_type is not PieceType.MAN:
                    continue

                piece = node.value
                for direction, neighbour in node.neighbors.items():
                    if neighbour.value is None and \
                        direction in self.allowed_directions(neighbour.value.color):
                        valid_moves.append(
                            Move(
                                (node.row, node.col),
                                (neighbour.row, neighbour.col),
                                captured=[],
                                next=None
                            )
                        )
                    if piece.color == neighbour.color:
                        continue

                    vacant_square = neighbour.neighbors.get(direction)
                    if vacant_square and vacant_square.value is None:
                        position = (vacant_square.row, vacant_square.col)
                        valid_moves.append(
                            Move(
                                (node.row, node.col),
                                position,
                                captured=[neighbour],
                                next=self._get_capture_move(piece, position)
                            )
                        )
