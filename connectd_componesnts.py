class solution(object):
  def components(self,n,nums):
    parent =[-1]*n
    res = n
    for edge in nums:
      src = edge[0]
      dest = edge[1]
      
      x= self.find_parent(parent,src)
      y = self.find_parent(parent,dest)
      if x!=y:
        res-=1
      	parent[x]=y
    return res

  def find_parent(self,parent,var):
  
    if parent[var]==-1:
      return var
    return self.find_parent(parent,parent[var])



def main():

  sol = solution()
  nums = [[0, 1], [2, 3], [3, 4]]
  print sol.components(5,nums)

if __name__=='__main__':
  main()
