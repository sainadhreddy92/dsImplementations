class Solution():
  def nessum(self,input):
    if not input:
      return 0

    return self.helper(input,1)



  def helper(self,input,depth):
    if not input:
      return 0
    su = 0
    for elem in input:
      if isinstance(elem,int):
        su+=elem*depth
      else:
        su+=self.helper(elem,depth+1)
    return su


def main():
  print Solution().nessum([[1,1],2,[1,1]])

if __name__=='__main__':
  main()
