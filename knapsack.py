def knapsack(W,Wt,Val,n):
  if n==0 or W==0:
    return 0
  
  if Wt[n-1]>W:
    return knapsack(W,Wt,Val,n-1)
  else:
    return max(Val[n-1]+knapsack(W-Wt[n-1],Wt,Val,n-1),knapsack(W,Wt,Val,n-1))

def main():
  Wt= [10, 20, 30]
  Val = [60, 100, 120]
  W=50
  n = len(Wt)
  print knapsack(W,Wt,Val,n)

if __name__=='__main__':
  main()
