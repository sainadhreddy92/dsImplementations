class Solution(object):
  def flipgame(self,input):
    if not input:
      return []
    res = []
    for i in range(1,len(input)):
      if input[i-1]=='+' and input[i]=='+':
        res.append(input[0:i-1]+'--'+input[i+1:])
    return res

def main():
  print Solution().flipgame("++++")


if __name__=='__main__':
  main()
