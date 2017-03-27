class solution():
  def factorcomb(self,n):
    res = []
    if n<=1:
      return res

    self.helper(n,res,2,[])
    return res



  def helper(self,n,res,start,tmp):
    if n<=1: 
      if len(tmp)>=1:
        res.append(tmp)
      return

    for i in range(start,n):
      if n%i==0:
        self.helper(n/i,res,i,tmp+[i])



def main():
  print solution().factorcomb(8)


if __name__=='__main__':
  main()
