def coinchange(coins,m,n):
  if n==0:
    return 1

  if n<0:
    return 0

  if m<=0 and n>=1:
    return 0

  return coinchange(coins,m-1,n)+coinchange(coins,m,n-coins[m-1])


def main():
  print coinchange([1,2,3],3,4)


if __name__=='__main__':
  main()
