from squardle_solver.node import Node

class Grid:
    def __init__(self, rows: list[str]):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = max(len(row) for row in rows)

        self.nodes = {
            (x, y): Node(self.get_char(x, y), x, y)
            for y in range(self.num_rows)
            for x in range(self.num_cols)
            if self.get_char(x, y) is not None
        }
        for (x, y), node in self.nodes.items():
            neighbours = [
                self.nodes[x + dx, y + dy]
                for dx in [-1, 0, 1]
                for dy in [-1, 0, 1]
                if (
                    ((dx, dy) != (0, 0))
                    and ((x + dx, y + dy) in self.nodes)
                )
            ]
            node.connect(neighbours)

    def get_char(self, x: int, y: int):
        if y < len(self.rows):
            row = self.rows[y]
            if x < len(row):
                c = row[x]
                if c.isalpha():
                    return c