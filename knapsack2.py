def knapsack(W,Wt,Val,n):
  res = []
  for _ in range(n+1):
    le = []
    for _ in range(W+1):
      le.append(0)
    res.append(le)

  for i in range(n+1):
    for j in range(W+1):
      if i==0 or j==0:
        res[i][j]=0
      elif Wt[i-1]>W:
        res[i][j] = res[i-1][j]
      else:
        res[i][j] = max(Val[i-1]+res[i-1][j-Wt[i-1]],res[i-1][j])
  return res[n][W]

def main():
  print knapsack(50,[10,20,30],[60,100,120],3)

if __name__=='__main__':
  main()
