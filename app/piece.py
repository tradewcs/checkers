from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1


class PieceType(Enum):
    MAN = 0
    KING = 1


class Piece:
    def __init__(
        self,
        color: Color,
        piece_type: PieceType = PieceType.MAN
    ) -> None:
        self.color: Color = color
        self.piece_type = piece_type

    def __str__(self) -> str:
        if self.piece_type == PieceType.MAN:
            return "○" if self.color == Color.WHITE else "●"
        return "◎" if self.color == Color.WHITE else "◉"

    def __repr__(self) -> str:
        color = "white" if self.color == Color.WHITE else "black"
        piece_type = "man" if self.piece_type == PieceType.MAN else "king"
        return f"{color} {piece_type}"
