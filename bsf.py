def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        print vertex
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
def main():
  graph = {0:set([1,2]),2:set([0,3]),3:set([3]),1:set([2])}
  visited = bfs(graph,2)
  print visited

if __name__=='__main__':
  main()
