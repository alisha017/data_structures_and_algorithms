# optimization of time complexity
# takes tree height into consideration

class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, value):
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value])  # optimization in find by path compression
        return self.parent[value]

    def union(self, value1, value2):
        parent_1 = self.find(value1)
        parent_2 = self.find(value2)

        if parent_1 != parent_2:
            if self.rank[parent_1] < self.rank[parent_2]:
                parent_1, parent_2 = parent_2, parent_1

            self.parent[parent_2] = parent_1  # assigning to the higher parent
            if self.rank[parent_1] == self.rank[parent_2]:
                self.rank[parent_1] += self.rank[parent_2]

    def is_connected(self, value1, value2):
        return self.find(value1) == self.find(value2)