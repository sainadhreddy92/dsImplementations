from random import randint
class solution(object):
  def partition(self,arr,start,end):
    pivot=randint(start,end)
    partindex=start
    arr[pivot],arr[end]=arr[end],arr[pivot]
    i=start
    while i<end:
      if  arr[i]<= arr[end]:
        arr[i],arr[partindex]=arr[partindex],arr[i]
        partindex+=1
      i+=1
    arr[partindex],arr[end]=arr[end],arr[partindex]
    return partindex  


  def quicksort(self,arr,start,end):
    if start>end:
      return
    partitionindex = self.partition(arr,start,end)
    self.quicksort(arr,start,partitionindex-1)
    self.quicksort(arr,partitionindex+1,end)
    return arr
    

def main():
  arr = [1,5,3,8,2]
  sol = solution()
  print sol.quicksort(arr,0,4)

if __name__=='__main__':
  main()
