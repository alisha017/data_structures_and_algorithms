import heapq


def prim(graph, start):
    # Initialize the MST and visited set
    mst = set()
    visited = {start}
    # Initialize the heap with the edges emanating from the start node
    edges = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start].items()
    ]
    heapq.heapify(edges)

    while edges:
        # Pop the edge with the smallest weight
        weight, parent, vertex = heapq.heappop(edges)
        if vertex not in visited:
            # Add the edge to the MST and mark the vertex as visited
            mst.add((parent, vertex, weight))
            visited.add(vertex)
            # Add the edges emanating from the newly visited vertex to the heap
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, vertex, neighbor))

    return mst
