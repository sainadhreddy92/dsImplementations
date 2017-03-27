def stringpermu(string):
  if not string:
    return []
  res = []
  string = list(string)
  helper(string,res,0)
  return res

def helper(string,res,pos):
  if pos>=len(string):
    res.append(''.join(string))

  for i in range(pos,len(string)):
    string[i],string[pos]=string[pos],string[i]
    helper(string,res,pos+1)
    string[i],string[pos]=string[pos],string[i]



def main():
  print stringpermu('abc')
  

if __name__=='__main__':
  main()
