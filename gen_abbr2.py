class solution(object):
  def genabbr(self,word):
    res = []
    self.helper(word,res,0,'',0)
    return res

  def helper(self,word,res,pos,curr,count):
    if pos==len(word):
      if count>0:
        curr=curr+str(count)
      res.append(curr)
      return

    self.helper(word,res,pos+1,curr,count+1)
    if count>0:
      self.helper(word,res,pos+1,curr+str(count)+word[pos],0)
    else:
      self.helper(word,res,pos+1,curr+word[pos],0)


def main():
  sol = solution()
  word='abcd'
  res= sol.genabbr(word)
  print res


if __name__=='__main__':
  main()

