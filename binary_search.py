class binarysearch(object):
  def upperbound(self,arr,low,high,key):
    if low>high:
      return low
    
    mid = low+ (high-low)/2

    if arr[mid]>key:
      return self.upperbound(arr,low,mid-1,key)
    else:
      return self.upperbound(arr,mid+1,high,key)

  def lowerbound(self,arr,low,high,key):
    if low>high:
      return low
    mid = low + (high-low)/2
    
    if arr[mid]>=key:
      return self.lowerbound(arr,low,mid-1,key)
    else:
      return self.lowerbound(arr,mid+1,high,key)

def main():
  bs = binarysearch()
  arr = [1,2,3,4,5,6,7,8,9,9,9,9]
  low = bs.lowerbound(arr,0,11,9)
  high = bs.upperbound(arr,0,11,9)
 
  print arr[low:high]

if __name__=='__main__':
  main()



