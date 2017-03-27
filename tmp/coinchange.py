def coinchange(coins,Tot,n):
  res = []


  for i in range(len(coins)):
    le = []
    for j in range(Tot+1):
      le.append(0)
    res.append(le)

  for i in range(len(coins)):
    res[i][0]=1

  for i in range(len(coins)):
    for j in range(1,Tot+1):
      if j >= coins[i]:
        res[i][j]=res[i-1][j]+res[i][j-coins[i]]
      else:
        res[i][j] = res[i-1][j]

  return res[len(coins)-1][Tot]



def main():
  print coinchange([1,2,3],4,3)


if __name__=='__main__':
  main()
