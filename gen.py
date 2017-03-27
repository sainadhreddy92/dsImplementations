class solution(object):
  def genabbr(self,word):
    if not word:
      return []

    res = []
    self.helper(word,res,'',0,0)

    return res


  def helper(self,word,res,tmp,count,start):
    if start==len(word):
      if count>0:
        tmp=tmp+str(count)
      res.append(tmp)
      return 

    self.helper(word,res,tmp,count+1,start+1)

    if count>0:
      self.helper(word,res,tmp+str(count)+word[start],0,start+1)
    else:
      self.helper(word,res,tmp+word[start],0,start+1)

def main():
  sol = solution()
  word = 'abcd'
  print sol.genabbr(word)


if __name__ == '__main__':
  main()
