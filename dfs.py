
def dfs(graph, start,visited):
  if start not in visited:
    visited.append(start)
    print start
    for vertex in graph[start]:
      if vertex not in visited:
        dfs(graph,vertex,visited)

def main():
  graph = {0:[1,2],2:[0,3],3:[3],1:[2]}
  visited = []
  dfs(graph,2,visited)
  print visited

if __name__=='__main__':
  main()
