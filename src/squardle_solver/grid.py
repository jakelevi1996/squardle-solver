from squardle_solver.node import Node
from squardle_solver.word_tree import WordTree

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

    def find_neighbours(
        self,
        node: Node,
        subtree: WordTree,
        history: list[Node],
        min_len: int,
    ):
        for neighbour in node.edges:
            if neighbour not in history:
                is_word = (neighbour.c in subtree.leaf_str)
                if is_word and ((len(history) + 1) >= min_len):
                    path = history + [neighbour]
                    print("".join(n.c for n in path))
                if neighbour.c in subtree.subtree_dict:
                    self.find_neighbours(
                        neighbour,
                        subtree.subtree_dict[neighbour.c],
                        history + [neighbour],
                        min_len,
                    )

    def solve(self, word_tree: WordTree, min_len: int):
        for node in sorted(self.nodes.values()):
            self.find_neighbours(
                node,
                word_tree.subtree_dict[node.c],
                [node],
                min_len,
            )
