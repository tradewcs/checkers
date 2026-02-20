from pieces import Piece


class Node:
    def __init__(self, value: Piece | None = None):
        self.value: Piece | None = value
        neighbours: list[Node] | None = None


class Board:
    def __init__(self, width: int = 8, height: int = 8):
        self.width = width
        self.height = height
        self.board: list[Node] = []


    def init_board(self):
        for _ in range(width // 2):
            self.board.append(Node())
        for _ in range(width // 2 - 1):
            for node in self.board[-self.width // 2:]:
                node.neighbours
