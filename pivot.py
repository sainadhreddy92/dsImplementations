class solution(object):
  def pivot(self,nums,left,right):

    while left<=right:
      if nums[left]<nums[right]:
        return left-1
    
      else:
        mid = (left+right)/2
        if nums[mid]>nums[right]:
          if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
            return mid
          else:
            left = mid+1
        else:
          right = mid
    return -1




 



def main():
    sol = solution()
    nums = [3,4,5,1,2]
    print sol.pivot(nums,0,4)
    


if __name__=='__main__':
  main()
