
class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.size = [0] * n

    def find(self, value):
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value])  # optimization in find by path compression
        return self.parent[value]

    def union(self, value1, value2):
        parent_1 = self.find(value1)
        parent_2 = self.find(value2)

        if parent_1 != parent_2:
            if self.size[parent_1] < self.size[parent_2]:
                parent_1, parent_2 = parent_2, parent_1

            self.parent[parent_2] = parent_1
            self.size[parent_1] += self.size[parent_2]

            '''
            if (size[a] < size[b])
            swap(a, b);
            parent[b] = a;
            size[a] += size[b];
            '''

    def is_connected(self, value1, value2):
        return self.find(value1) == self.find(value2)