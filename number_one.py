def numberofones(row):
  low = 0
  high = len(row)-1
  
  if row[low]==1:
    return high-low+1
  if row[high]==0:
    return 0

  while low<high:
    mid = low+(high-low)/2
    
    if row[mid]==1:
      high= mid
    else:
      low =mid+1

  return len(row)-1-low+1

def main():
  row=[0,0,0,1]
  print numberofones(row)


if __name__=='__main__':
  main()
