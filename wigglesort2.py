def wigglesort(nums):
  if not nums:
    return nums

  for i in range(1,len(nums)):
    if ( i%2==1 and nums[i]<nums[i-1]) or ( i%2==0 and nums[i]>nums[i-1]):
      nums[i],nums[i-1]=nums[i-1],nums[i]
  return nums


def main():
  nums =[3,5,2,1,6,4]
  print wigglesort(nums)


if __name__=='__main__':
  main()
