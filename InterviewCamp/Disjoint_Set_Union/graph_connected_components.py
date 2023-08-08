class Union_Find:
    def __init__(self, grid) -> None:
        row = len(grid)
        col = len(grid[0])
        self.parent = [0] * (row * col)
        self.rank = [-1] * (row * col)
        self.connected_components = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.parent[i * col + j] = (i * col + j)
                    self.connected_components += 1
                self.rank[i * col + j] = 0

    def find_set(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find_set(self.parent[vertex])
        return self.parent[vertex]

    def union_set(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x

            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += self.rank[root_y]

            self.connected_components -= 1


def check_oob(x, y, max_x, max_y):
    if x < 0 or x >= max_x or y < 0 or y >= max_y:
        return True
    return False


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        djs = Union_Find(grid)
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    points = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    for point in points:
                        if not check_oob(point[0], point[1], row, col) and grid[point[0]][point[1]] == "1":
                            djs.union_set(i * col + j, point[0] * col + point[1])

        return djs.connected_components
