from typing import List


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))

    def find(self, value):
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value]) # optimization in find by path compression
        return self.parent[value]

    def union(self, value1, value2):
        parent_1 = self.find(value1)
        parent_2 = self.find(value2)

        if parent_1 != parent_2:
            self.parent[value1] = parent_2

    def is_connected(self, value1, value2):
        return self.find(value1) == self.find(value2)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union_find_nodes = UnionFind(n)

        for edge in edges:
            union_find_nodes.union(*edge)

        return union_find_nodes.is_connected(source, destination)