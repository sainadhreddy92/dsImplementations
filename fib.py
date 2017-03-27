def fib(n):
  if n<=0:
    return 0

  if n==1:
    return 1

  p = 0
  q = 1
  r = 1
  for _ in range(n-1):
    r = p+q
    p = q
    q = r
  return r

def main():
  for i in range(10):
    print fib(i)

if __name__=='__main__':
  main()     
