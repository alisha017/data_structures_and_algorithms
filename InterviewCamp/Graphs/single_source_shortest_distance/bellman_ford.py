from typing import List, Tuple, Dict


class Graph:
    def __init__(self, vertices:List[int]) -> None:
        self.vertices = vertices
        self.edges: List[Tuple[int]]= []

    def add_edge(self, source, dest, weight):
        self.edges.append((source, dest, weight))

    def bellman_fords_algo(self, source, destination, k):
        previous:Dict[int, int] = [float('inf') for node in self.vertices]
        previous[source] = 0
        current = [float('inf') for node in self.vertices]

        for _ in range(k+1):
            current[source] = 0
            for src, dest, weight in self.edges:
                # print(f"Current val: i = {_}, {src}, {dest}, {weight}")
                if previous[src] != float('inf'):
                    # if dest == destination:
                    #     print(f"\tchanging from {previous[dest]} to {previous[src]+weight}")
                    current[dest] = min(current[dest], previous[src] + weight)
            print(f"previous:{previous}\ncurrent:{current}")
            previous = current.copy()

        return previous[destination] if previous[destination] != float("inf") else -1
