def foursum(arr):
  i,j,k,l=0,0,0,0
  res = []
  sum_dict={}
  while i<len(arr)-1:
    j=i+1
    while j<len(arr):
      su = arr[i]+arr[j]
      if su not in sum_dict:
        sum_dict[su]=[[i,j]]
      else:
        sum_dict[su].append([i,j])
      j+=1
    i+=1

  print sum_dict  

  for key in sum_dict:
    if len(sum_dict[key])>1:
      res.append([sum_dict[key]])
  return res
    

def main():
  arr = [1,2,3,4,-1,6]
  print foursum(arr)


if __name__=='__main__':
  main()
