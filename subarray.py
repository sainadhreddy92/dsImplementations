def gensubarray(nums):
  res = []
  helper(res,[],0,nums)
  return res



def helper(res,tmp,start,nums):
  if start>len(nums):
    return
  if tmp:
    res.append(tmp)
    if start<len(nums):
      helper(res,tmp+[nums[start]],start+1,nums)
  else:
    for i in range(start,len(nums)):
      helper(res,tmp+[nums[i]],i+1,nums)  


def main():
  print gensubarray([1,2,3,4,5])

if __name__=='__main__':
  main()
