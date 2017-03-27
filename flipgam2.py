class solution():
  def flipgame2(self,string):
    result = {}
    return self.helper(string,result)



  def helper(self,string,result):
    if string in result:
      return result[string]


    for i in range(1,len(string)):
      if string[i-1]=='+' and string[i]=='+':
        tmp = string[:i]+'--'+string[i+1:]
        if not self.helper(tmp,result):
          result[tmp]=True
          return True

    result[string]=False
    return False


def main():
  string='++++'
  print solution().flipgame2(string)


if __name__=='__main__':
  main()          
