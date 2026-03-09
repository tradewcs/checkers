from __future__ import annotations
from dataclasses import dataclass

from app.board import Node


@dataclass
class Move:
    from_position: tuple[int, int]
    to_position: tuple[int, int]
    captured: list[Node] | None
    next: Move | None
