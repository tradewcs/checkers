from enum import Enum


class PieceColor(Enum):
    WHITE = 0
    BLACK = 1


class PieceType(Enum):
    MAN = 0
    KING = 1


class Piece:
    def __init__(
        self,
        color: PieceColor,
        piece_type: PieceType = PieceType.MAN
    ) -> None:
        self.color: PieceColor = color
        self.piece_type = piece_type

    def __str__(self) -> str:
        if self.piece_type == PieceType.MAN:
            return "○" if self.color == PieceColor.WHITE else "●"
        return "◎" if self.color == PieceColor.WHITE else "◉"

    def __repr__(self) -> str:
        color = "white" if self.color == PieceColor.WHITE else "black"
        piece_type = "man" if self.piece_type == PieceType.MAN else "king"
        return f"{color} {piece_type}"
