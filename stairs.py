def climb(n):
  if n<=0:
    return 0
  elif n==1 or n==2:
    return n
  else:
    return climb(n-1)+climb(n-2)

def main():
  for i in range(10):
    print climb(i)

if __name__=='__main__':
  main()
