class Solution(object):
  def issquare(self,words):
    if not words:
      return True
    
    for i in range(len(words)):
      for j in range(len(words[i])):
        if j>=len(words) or i>=len(words[j]) or  words[i][j]!=words[j][i]:
          return False
    return True
        

def main():
  words = [
  "abcd",
  "bnrt",
  "crmy",
  "dtye",
  "pqrs"
]

  sol = Solution()
  print sol.issquare(words)


if __name__=='__main__':
  main()
