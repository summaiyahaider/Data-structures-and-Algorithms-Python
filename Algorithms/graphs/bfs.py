'''
In BFS, we traverse one level at a time and then jump to the next level. In a graph, the traversal can start from any node and cover all the nodes level-wise.
'''

'''
Data-Structures Used: queue, array
Algorithm:
1) pick a vertex
2) if it is not in seen go to step 3
3) add the vertex to queue, set, result-array
4) while q is not empty , pop the queue and traverse the vertices of popped vertex and do step 2 and 3
'''



from collections import deque

def bfs(graph, seen, q, vertex, res):
    if vertex in seen: return
    q.append(vertex)
    seen.add(vertex)
    res.append(vertex)
    while q:
        currVertex = q.popleft()
        for v in graph[currVertex]:
            if v not in seen:
                seen.add(v)
                res.append(v)
                q.append(v)


def bfsOfGraph(v, adj):
    q = deque()
    res = []
    seen = set()
    for vertex in range(v):
      bfs(adj, seen, q, vertex, res)
    return res
