import sys
import heapq

def dijkstra(graph, src, goal):
    unseen_nodes = {}
    



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

    answer = dijkstra(graph, src, dest)
    print(f"The shortest path from node {src} to node {dest} is through the nodes {answer[0]} "
          f"and the minimum cost is {answer[1]}")