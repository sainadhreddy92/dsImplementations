import sys

class Solution(object):
  def flip(self,string):
    res = []
    if len(string)<=1:
      return res
    string = list(string) 
    for i in range(len(string)-1):
      if string[i]==string[i+1]=='+':
        string[i]='-'
        string[i+1]='-'
        res.append("".join(string))
        string[i]='+'
        string[i+1]='+'
    return res



def main():
  sol = Solution()
  print sol.flip(sys.argv[1])

if __name__=='__main__':
  main()
