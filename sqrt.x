class solution(object):
  def sqrt(self,x):
    r = x
    while r*r>x:
      r = (r + x/r)/(2*1.0)
    return r



def main():
  x = 25
  sol = solution()
  print sol.sqrt(x)

if __name__=='__main__':
  main()
