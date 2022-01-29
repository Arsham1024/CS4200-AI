import sys
import heapq

def dijkstra(graph, src, goal):
    inf = sys.maxsize # some kind of infinity
    unseen_nodes = graph
    shortest_distance = {}
    track_predecessor = {}
    path = []

    # initialize all the nodes to inf except for the first node
    for node in unseen_nodes:
        shortest_distance[node] = inf
    shortest_distance[src] = 0

    # While we still have unseen nodes keep going
    while unseen_nodes:

        # current best node
        minimum_node = None

        # Just trying to find the minimum node out of all the ones in graph to consider
        for node in unseen_nodes:
            if minimum_node is None:
                minimum_node = node

            #     we just want to figure out which node that is currently accesible is the miimum node
            elif shortest_distance[node] < shortest_distance[minimum_node]:
                minimum_node = node

        # get all the path options to the selected node
        path_options = graph[minimum_node].items()

        for child, weight in path_options:
            print(child, weight)
            if weight + shortest_distance[minimum_node] < shortest_distance[child]:
                shortest_distance[child] = weight + shortest_distance[minimum_node]

                track_predecessor[child] = minimum_node
        unseen_nodes.pop(minimum_node)

    current = dest
    while current != src:
        path.insert(0, current)
        current = track_predecessor[current]

    path.insert(0, src)
    # at the end return this
    return path, shortest_distance[goal]


if __name__ == '__main__':
    graph = {
        'A': {'C': 3, 'F': 2},
        'B': {'E': 2, 'D': 1, 'F': 6, 'G': 2},
        'C': {'A': 3, 'D': 4, 'E': 1, 'F': 2},
        'D': {'B': 1, 'C': 4},
        'E': {'C': 1, 'F': 3, 'B': 2},
        'F': {'A': 2, 'C': 2, 'E': 3, 'B': 6, 'G': 5},
        'G': {'F': 5, 'B': 2}
    }
    src = 'A'
    dest = 'B'

    answer = dijkstra(graph, src, dest)
    print(f"The shortest path from node {src} to node {dest} is through the nodes {answer[0]} "
          f"and the minimum cost is {answer[1]}")