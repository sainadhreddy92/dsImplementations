class merge_sort(object):
  def msort(self,array):
    if not array or len(array)<2:
      return 
    mid = len(array)/2
    left_array = array[0:mid]
    right_array = array[mid:]
    self.msort(left_array)
    self.msort(right_array)
    
    self.merge(array,left_array,right_array)



  def merge(self,array,left,right):
    i1=i2=i3=0
    
    while i1<len(left) and i2<len(right):
      if left[i1]<=right[i2]:
        array[i3] = left[i1]
        i3+=1
        i1+=1
      else:
        array[i3]= right[i2]
        i3+=1
        i2+=1
    while i1<len(left):
      array[i3]=left[i1]
      i3+=1
      i1+=1
    while i2<len(right):
      array[i3] = right[i2]
      i3+=1
      i2+=1

def main():
  array = [9,5,8,3,4,2,6,1,7]
  ms = merge_sort()
  ms.msort(array)
  print array

if __name__=='__main__':
  main()

