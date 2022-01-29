import heapq
import sys

def dijkstra(graph, src, dest):
    # max size
    inf = sys.maxsize
    shortest_distance  = {} # records the cost to reach to that specific node, updated as we move along graph
    track_predecessor = {} # keep track of path that lead to this node
    unseen_nodes = graph
    path = [] # optimal route

    # initializing all the nodes to inf except for the start node
    for node in unseen_nodes:
        shortest_distance[node] = inf
    shortest_distance[src] = 0

#     Run until all unseen nodes are gone
    while unseen_nodes:
        min_dist_node = None
        # if the node is in unseen node we need to traverse it
        for node in unseen_nodes:
            # at the begining when min dist is none assgin the current node to it to start the process
            if min_dist_node is None:
                min_dist_node = node
            # if the shortest distance to the node we are considering is less than the shortest distance to
            # the minimum distance node so far then replace the node
            # basically means that if the current distance is shorter then we found a better option than the last one.
            elif shortest_distance[node] < shortest_distance[min_dist_node]:
                min_dist_node = node

        # These are the nodes we can go from the current best node / min dist node
        path_options = graph[min_dist_node].items()

        # go through all the option to pick the best one
        for child , weight in path_options:
            if weight + shortest_distance[min_dist_node] < shortest_distance[child]:
                shortest_distance[child] = weight+shortest_distance[min_dist_node]
                # keep track of the predecessor
                track_predecessor[child] = min_dist_node

        unseen_nodes.pop(min_dist_node)


if __name__ == '__main__':
    graph = {
        'A' : {'B': 2, 'C':4},
        'B' : {'A': 2, 'C':3, 'D':8},
        'C' : {'A': 4, 'B':3, 'E': 5 , 'D': 2},
        'D' : {'B': 8, 'C':2, 'E': 11 , 'F': 22},
        'E' : {'C': 5, 'D':11, 'F': 1},
        'F' : {'D': 22, 'E':1}
    }
    src = 'A'
    dest = 'F'
    dijkstra(graph, src, dest)