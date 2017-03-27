import sys


class Solution(object):
  def nested(self,nestedlist):
    depth = self.find_depth(nestedlist)
    return self.helper(nestedlist,depth)
	

  def helper(self,itemlist,depth):
    sum=0
    for item in itemlist:
      if isinstance(item,int):
        sum+=depth*item
      else:    
        sum+=self.helper(item,depth-1)
    return sum


  def find_depth(self,nestedlist):
    depth=0
    if not isinstance(nestedlist,int):
      for item in nestedlist:
        depth = max(self.find_depth(item),depth)
      return 1+depth
    else:
      return 0




def main():
  nestedlist = [[1,1],2,[1,1]]
  sol = Solution()
  print sol.nested(nestedlist)
  #print sol.find_depth(nestedlist)

if __name__=='__main__':
  main()
