class solution(object):
  def genabbr(self,string):
    if not string or len(string)==0:
      return []
    res =[]
    self.helper(res,0,'',0,string)

    return res

  def helper(self,res,n,tmp,count,string):
    if n==len(string):
      if count:
       res.append(tmp+str(count))
      else:
       res.append(tmp)

    else:
      self.helper(res,n+1,tmp,count+1,string)
      if count:
        self.helper(res,n+1,tmp+str(count)+string[n],0,string)
      else:
        self.helper(res,n+1,tmp+string[n],0,string)
      


def main():
  sol = solution()
  print sol.genabbr('word')

if __name__=='__main__':
  main()
