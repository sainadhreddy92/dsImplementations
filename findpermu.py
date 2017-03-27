class Solution(object):
  def findpem(self,st):
    res = [0]*(len(st)+1)
    for i in range(len(st)+1):
      res[i]=i+1
    
    i=0
    while i<len(st):
      low = i
      if st[i]=='D':
        while i<len(st) and  st[i]=='D':
          i+=1
          high = i
        self.rev(low,high,res)
      i+=1
    return res

  def rev(self,start,end,res):
    while start<end:
      res[start],res[end]=res[end],res[start]
      start+=1
      end-=1


def main():
  st = 'ID'
  print Solution().findpem(st)   


if __name__=='__main__':
  main()  
