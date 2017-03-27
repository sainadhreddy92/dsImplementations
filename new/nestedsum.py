class Solution(object):
  def nestedsum(self,nestedlist):
    return self.helper(nestedlist,1)

  def helper(self,nestedlist,depth):
    su=0
    for item in nestedlist:
      if isinstance(item,int):
        su+=item*depth
      else:
        su+=self.helper(item,depth+1)
    return su


  def nestedsum2(self,nestedlist):
    depth = self.finddepth(nestedlist)
    return self.helper2(nestedlist,depth)

  def helper2(self,nestedlist,depth):
    su=0
    for item in nestedlist:
      if isinstance(item,int):
        su+=depth*item
      else:
        su+=self.helper2(item,depth-1)
    return su


  def finddepth(self,nestedlist):
    depth=0
    if not isinstance(nestedlist,int):
      for item in nestedlist:
        depth = max(depth,self.finddepth(item))
      return 1+depth
    else:
        return 0

def main():
  sol = Solution()
  print sol.nestedsum2([1,[4,[6]]])

if __name__=='__main__':
  main()
