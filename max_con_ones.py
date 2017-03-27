class Solution(object):
  def maxones(self,nums):
    i=j=zero=0
    maxlen = 0
    while j < len(nums):
      if nums[j]==0:
        zero+=1
      
      while zero>1:
        if nums[i]==0:
          zero-=1
        i+=1
      
      maxlen = max(j-i+1,maxlen)
      j+=1
    return maxlen


def main():
  sol = Solution()
  nums = [1,1,0,1,0,0,0]
  print sol.maxones(nums)

if __name__=='__main__':
  main()
     
