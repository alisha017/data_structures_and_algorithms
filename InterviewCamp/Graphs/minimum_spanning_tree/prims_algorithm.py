from typing import List
class Graph:
    def __init__(self, vertices) -> None:
        self.vertices_num = vertices
        self.graph = []

    def add_edge(self, edge: List[int]):
        self.graph.append(edge)

    def find_set(self, parent, value):
        if value != parent[value]:
            parent[value] = self.find_set(parent, parent[value])
        return parent[value]

    def union_set(self, parent, rank, x, y):
        root_x = self.find_set(parent, x)
        root_y = self.find_set(parent, y)

        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x

            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1

    def kruskals_mst(self):
        result = []

        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = {}
        rank = {}

        for node in range(1, self.vertices_num + 1):
            parent[node] = node
            rank[node] = node

        while e < self.vertices_num - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            # print(f"u, v, w = {(u, v, w)}, parent:{parent}")
            u_root = self.find_set(parent, u)
            v_root = self.find_set(parent, v)
            # print(f"u_root:{u_root}, v_root:{v_root}")

            if u_root != v_root:
                e += 1
                result.append([u, v, w])
                self.union_set(parent, rank, u_root, v_root)

        if e < self.vertices_num - 1:
            return -1
        print("\n", len(result), result)
        min_cost = 0
        for edge in result:
            min_cost += edge[-1]
        return min_cost