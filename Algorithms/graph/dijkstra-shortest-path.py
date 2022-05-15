from heapq import *

'''
Dijkstra's Algorithm finds the shortest path between a given node (which is called the "source node") and all other nodes in a graph. This algorithm uses the weights of the edges to find the path that minimizes the total distance (weight) between the source node and all other nodes.
'''

'''
Data-Structures Used: set, min-heap, dictionary
Algorithm:
1) Initially, the distance from source-node to all other nodes is 'Infinity', because we dont know if all the nodes are reachable from source-node
2) add the source-node to min-heap with path 0 (each item in the heap stores, path and the node. path represents the distance it took to get to the node. we pop from min-heap based on path i.e distance)
3) while the heap is not empty, do step 4 and 5
4) pop from min-heap and if the node 'u' is not already seen or visited, add it to seen and we found shortest path from source-node to the node 'u'. go to step 5
5) traverse the edges of the 'u' and push them to the min-heap, with path + distance 
'''

'''
Note: The graph is represented using a dictionary of key-value pairs, the key being vertice 'u' and the value being a list of edges with weights.

dijsktras algorithm works for both directed and un-directed graph 

Ex: graph = {'a': [('b', 2), ('c', 4)]}

    'a'
 2  / \ 4
  /    \
'b'    'c'

'''

def find_shortest_path(graph, n, source_node):
    # initialize distance map from source
    short_distance_map = {i: float('inf') for i in range(1, n+1)}
    # to keep track of visited nodes
    seen = set()
    # min-heap to pop out the min-path node
    heap = []
    heap.append((0, source_node))
    while heap:
        path, u = heappop(heap)
        if u not in seen:
            # if not seen we fround shortest-distance from source-node to this node
            seen.add(u)
            short_distance_map[u] = path
            # bfs, traverse the edges of u
            for x in graph[u]:
                v, distance = x
                heappush(heap, (distance+path, v))
    return short_distance_map