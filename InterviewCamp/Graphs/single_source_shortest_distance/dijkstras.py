import heapq


def dijkstras_distance(graph, start, total_nodes):
    distance_node_dict = {node:float('inf') for node in graph}
    prev_node_dict = {node: None for node in graph}
    visited = set()

    distance_node_dict[start] = 0
    queue = [(0, start)]

    while queue:
        curr_distance, curr_node = heapq.heappop(queue)

        if curr_node in visited:
            continue

        visited.add(curr_node)

        for neighbour, weight in graph[curr_node].items():
            distance = curr_distance + weight
            if distance < distance_node_dict[neighbour]:
                distance_node_dict[neighbour] = distance
                prev_node_dict[neighbour] = curr_node
                heapq.heappush(queue, (distance, neighbour))

    if len(visited) != total_nodes:
        return -1

    return distance_node_dict
