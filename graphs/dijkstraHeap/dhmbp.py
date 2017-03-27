from graph import * 
from dijkstra import *
from heap import *
from vertex import *
from globals import *

class mbp():
  def mbp_calc(self,weight,source,dest):
    global_def = globals()
    vertex_heap = heap(global_def.vertices)
    vertex_heap.heap_array=[0]*global_def.vertices
    vertex_heap.heap_array[0] = source
    
    for i in range(global_def.vertices):
      if i<=source:
        vertex_heap.heap_array[i]=i-1
      else:
        vertex_heap.heap_array[i]=i

    vertexes = []
    
    for i in range(global_def.vertices):
      vertexes.append(vertex())

    vertexes[source].bandwidth = global_def.WEIGHTRANGE+1 

    for l in range(global_def.vertices):
      index = vertex_heap.peek()
      vertex_heap.delete(vertexes)
      for m in range(global_def.vertices):
        if weight[index][m]!=0:
          if vertexes[m].bandwidth < min(vertexes[l].bandwidth,weight[l][m]):
            vertexes[m].bandwidth = min(vertexes[l].bandwidth,weight[l][m])
            vertexes[m].predec = l
            vertex_heap.update(vertexes,m)

    print "Path is :"

    while dest!= -1:
      print vertexes[dest].predec
      dest = vertexes[dest].predec

def main():
  graph_def = graphs()
  global_def = globals()

  weight_matrix=[]
  for i in range(global_def.vertices):
    le = []
    for j in range(global_def.vertices):
      le.append(0)
    weight_matrix.append(le)
  
  k =0
  while k<global_def.vertices:
    while (graph_def.CalcRowsum(weight_matrix,k)!=global_def.degree2):
      weight_matrix = graph_def.initialize(weight_matrix)
      k=0
      weight_matrix = graph_def.random_generate2(weight_matrix)
    k+=1

  print weight_matrix

  mbp().mbp_calc(weight_matrix,25,26)

if __name__ == '__main__':
  main() 
