class solution(object):
  def magicstring(self,n):
    res = '122'
    tail = 2
    while len(res)<n:
      gen = int(res[-1])^3
      mul = int(res[tail])
      res.append(gen*mul)
      tail+=1
    return res[:n]

def main():
  sol = solution()
  print self.magicstring(10)

if __name__=='__main__':
  main()
