'''
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG
'''

'''
Data-Structures Used: set, stack
Algorithm: 
1) Select a vertex
2) Check if the selected vertex is in the set if it is not got to step-3
3) Add the vertex to set and traverse other nodes of the vertex recursively
4) Add the vertex to stack
'''

def topological_sort(graph, seen, stk, current_vertex):
  if current_vertex not in seen:
    seen.add(current_vertex)
    current_vertex_children = graph[current_vertex]
    for child in current_vertex_children:
      topological_sort(graph, seen, stk, child)
      stk.append(current_vertex)


def topoSort(v, graph):
    stk = []
    seen = set()
    for vertex in range(v):
      topological_sort(graph, seen, stk, vertex)
    stk.reverse()
    return stk
