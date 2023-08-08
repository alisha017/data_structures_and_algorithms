class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find_set(self, value) -> int:
        if value != self.parent[value]:
            self.parent[value] = self.find_set(self.parent[value])
        return self.parent[value]

    def union_set(self, a, b) -> bool:   # False means there is no cycle, True means a cycle has been detected
        root_1 = self.find_set(a)
        root_2 = self.find_set(b)
        # print(f"a:{a}, b:{b}, root_a:{root_1}, root_b:{root_2}, parent:{self.parent}")
        if root_1 != root_2:
            if self.rank[root_1] < self.rank[root_2]:
                root_1, root_2 = root_2, root_1

            self.parent[root_2] = root_1
            if self.rank[root_1] == self.rank[root_2]:
                self.rank[root_1] += self.rank[root_2]

            return False

        return True

    def set_count(self) -> int:
        count = 0
        for i in range(len(self.parent)):
            if i == self.parent[i]:
                count += 1

        return count

    def is_disconnected(self) -> bool:
        count = self.set_count()
        if count > 1:
            return True
        return False
