class solution(object):
  def find_depth(self,nestedlist):
    depth = 0
    if not nestedlist:
      return depth
    
    if isinstance(nestedlist,list):
      for item in nestedlist:
        depth = max(depth,self.find_depth(item))
      return 1+depth
    else:
      return 0



def main():
  nestedlist = [4,[6,[7]]]
  sol = solution()
  print sol.find_depth(nestedlist)


if __name__=='__main__':
  main()
