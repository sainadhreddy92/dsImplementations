class solution():
  def genabbr(self,string):
    res = []
    if not string:
      return res

    self.helper(string,'',0,res,0)
    return res
      

  def helper(self,string,tmp,pos,res,count):
    if pos==len(string):
      if count:
        tmp+=str(count)
      res.append(tmp)
      return

    if count:
      self.helper(string,tmp,pos+1,res,count+1)
      self.helper(string,tmp+str(count)+string[pos],pos+1,res,0)

    else:
      self.helper(string,tmp,pos+1,res,count+1)
      self.helper(string,tmp+string[pos],pos+1,res,0) 

def main():
  print solution().genabbr('word')

if __name__=='__main__':
  main()
