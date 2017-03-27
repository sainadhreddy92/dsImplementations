class solution(object):
  def factors(self,n):
    res=[]
    if n<=1:
      return []
    
    self.helper(res,[],n,2)
    return res[:-1]


  def helper(self,res,temp,n,start):
    if n==1:
      res.append(temp)
      return 

    i=start
    while i<=n or i==2:
      if n%i==0:
        self.helper(res,temp+[i],n/i,i)
      i+=1


def main():
  sol=solution()
  for i in range(1,32):
    print i,"--->",sol.factors(i)
  

if __name__=='__main__':
  main()      
