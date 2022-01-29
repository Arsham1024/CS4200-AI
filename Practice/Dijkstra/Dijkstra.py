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
        for child, weight in path_options:
            if weight + shortest_distance[min_dist_node] < shortest_distance[child]:
                shortest_distance[child] = weight+shortest_distance[min_dist_node]
                # keep track of the predecessor
                track_predecessor[child] = min_dist_node

        unseen_nodes.pop(min_dist_node)

    # We are going to trace back from the end to start
    # by this point we have found the destination.
    current_node = dest
    while current_node != src:
        path.insert(0, current_node)
        # This gives the next node to trace back
        current_node = track_predecessor[current_node]

    path.insert(0, src)

    # if the shortest distance to goal is not inf means we found something better aka shortest path
    if shortest_distance[dest] != inf:
        return path, shortest_distance[dest]



if __name__ == '__main__':
    graph = {
        'A' : {'C': 3, 'F':2},
        'B' : {'E': 2, 'D':1, 'F':6, 'G':2},
        'C' : {'A': 3, 'D':4, 'E': 1 , 'F': 2},
        'D' : {'B': 1, 'C':4},
        'E' : {'C': 1, 'F':3, 'B': 2},
        'F' : {'A': 2, 'C':2, 'E':3 , 'B':6, 'G':5 },
        'G' : {'F': 5 , 'B': 2}
    }
    src = 'A'
    dest = 'B'
    print(dijkstra(graph, src, dest))