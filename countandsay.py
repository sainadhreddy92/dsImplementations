class solution():
  def count(self,n):
    if not n:
      return 0

    res = '1'

    if n==1:
      return res

    for _ in range(n-1):
      res = self.helper(res)
      print res
    return res



  def helper(self,res):
    res2 = ''

    i=0
    while i<len(res):
      count = 1
      while i+1<len(res) and res[i]==res[i+1]:
        count+=1
        i+=1
      res2+=str(count)+res[i]
      i+=1
    return res2
        

def main():
  print solution().count(6)


if __name__=='__main__':
  main()
