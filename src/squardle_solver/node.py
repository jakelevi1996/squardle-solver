class Node:
    def __init__(self, node_char: str, x: int, y: int):
        self.c = node_char
        self.x = x
        self.y = y
        self.edges: list[Node] = []

    def connect(self, others: list["Node"]):
        self.edges = sorted(self.edges + others)

    def to_tuple(self):
        return self.c, self.x, self.y

    def __hash__(self):
        return hash(self.to_tuple())

    def __eq__(self, other: "Node"):
        return self.to_tuple() == other.to_tuple()

    def __lt__(self, other: "Node"):
        return self.to_tuple() < other.to_tuple()

    def __repr__(self):
        edge_chars = "-".join(node.c for node in self.edges)
        return (
            "%s(%s, %s, %s, %s)"
            % (type(self).__name__, *self.to_tuple(), edge_chars)
        )
