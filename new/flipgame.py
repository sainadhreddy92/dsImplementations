class solution(object):
  def flipgame(self,string):
    res =[]
    string = list(string)
    i=0
    while i <len(string)-1:
      if string[i]=='+' and string[i+1]=='+':
        res.append(''.join(string[0:i])+"--"+''.join(string[i+2:]))
      i+=1

    return res


def main():
  sol = solution()
  print sol.flipgame("++++++++")

if __name__=='__main__':
  main()
