class quicksort(object):
  def partition(self,array,start,end):
    pindex = start
    pivot = array[end]
    for i in range(start,end):
      if array[i] <= pivot:
        array[i],array[pindex] = array[pindex],array[i]
        pindex+=1
    array[pindex],array[end] = array[end],array[pindex]
    return pindex

  def quick(self,array,start,end):
    if start<end:
      pindex = self.partition(array,start,end)
      self.quick(array,start,pindex-1)
      self.quick(array,pindex+1,end)
    #return array

def main():
  array = [7,2,1,6,8,5,3,4]
  sol = quicksort()
  sol.quick(array,0,7)
  print array

if __name__=='__main__':
  main()
