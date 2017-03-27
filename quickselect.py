class solution(object):
  def partition(self,arr,start,end):
    pivot= end
    i=start
    partindex=start
    while i<end:
      if arr[i]<=arr[pivot]:
        arr[i],arr[partindex]=arr[partindex],arr[i]
        partindex+=1
      i+=1
    arr[partindex],arr[pivot]=arr[pivot],arr[partindex]
    return partindex
 
  def quicksort(self,arr,start,end,k):
    if start>end:
      return -1
    partindex = self.partition(arr,start,end)
    if partindex==k:
      return arr[k]
    elif partindex>k:
      return self.quicksort(arr,start,partindex-1,k)
    else:
      return self.quicksort(arr,partindex+1,end,k)


def main():
  sol = solution()
  arr = [1,3,2,5,4]
  print sol.quicksort(arr,0,4,0)

if __name__=='__main__':
  main()
    
