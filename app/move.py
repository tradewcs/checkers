from dataclasses import dataclass

from app.Node import Node


@dataclass
class Move:
    from_position: tuple[int, int]
    to_position: tuple[int, int]
    captured: list[Node] | None
