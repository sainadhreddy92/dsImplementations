class solution(object):
  def istree(self,n,edges):
    parents = [-1]*n
    for edge in edges:
      x= self.find(parents,edge[0])
      y= self.find(parents,edge[1])
      if x==y:
        return False
      parents[x]=y
    return True

  
  def find(self,parents,x):
    if parents[x]==-1:
      return x
    else:
      return self.find(parents,parents[x])


def main():
  sol = solution()
  edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
  print sol.istree(5,edges)  
if __name__=='__main__':
  main()
