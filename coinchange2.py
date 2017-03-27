def coinchange(coins,m,n):
  res = [[0 for _ in range(m+1)] for _ in range(n+1)]

  res[0][0] = 1
  
  for j in range(1,m+1):
    res[0][j]=0

  for i in range(1,n+1):
    res[i][0]=1

  for i in range(1,n+1):
    for j in range(1,m+1):
      if j>=coins[i-1]:
        res[i][j]+=res[i][j-coins[i-1]]
      res[i][j]+=res[i-1][j]
  print res
  return res[n][m]

def main():
  print coinchange([2,5,3,6],10,4)


if __name__=='__main__':
  main()
