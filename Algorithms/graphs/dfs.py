'''
 The algorithm starts by selecting some arbitrary node in a graph and explores as far as possible along each branch before backtracking.
'''

'''
Data-Structures Used: set, array
Algorithm:
1) pick a vertex
2) if it is not in the set add it to result and go to step 3
3) trvarse the vertices connected to the vertex recursively
'''


def depth_first_search(graph, currVertex, seen, result):
  if currVertex in seen: return
  seen.add(currVertex)
  result.append(currVertex)
  for vertex in graph[currVertex]:
    depth_first_search(graph, vertex, seen, result)


# main function 
def dfs(v, graph):
  result = []
  seen = set()
  for vertex in range(v):
    depth_first_search(graph, vertex, seen, result)
  return result

print(dfs(5, [[1, 4], [2, 3, 4], [1, 3], [1, 2, 4], [0, 1, 3]]))