class Solution(object):
  def permu(self,string):
    if not string:
      return []
    res = []
    self.helper(string,'',res)
    return res
 
  def helper(self,string,tmp,res):
    if not string:
      res.append(tmp)
    
    for i in range(len(string)):
      self.helper(string[:i]+string[i+1:],tmp+string[i],res)



def main():
  sol = Solution()
  print sol.permu('abc')

if __name__=='__main__':
  main()
