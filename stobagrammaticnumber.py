class Solution():
  def stob(self,nums):
    stob_dict={'0':'0','1':'1','8':'8','6':'9','9':'6'}
    if not nums:
      return True
    left = 0
    right = len(nums)-1


    while left<=right:
      if stob_dict[nums[left]]!=stob_dict[nums[right]]:
        return False
      left+=1
      right-=1
    return True


def main():
  sol = Solution()
  print sol.stob('18')


if __name__=='__main__':
  main()   
