class solution(object):

  def nestedsum(self,nums):
    if not nums:
      return 0

    su=0
    depth=1
    return self.helper(nums,su,depth)

  def helper(self,nums,su,depth):
    for num in nums:
      if isinstance (num,int):
        su+= depth*num
      else:
        su+= self.helper(num,0,depth+1)
    return su


def main():
  sol = solution()
  nums =[1,[4,[6]]]

  print sol.nestedsum(nums)


if __name__=='__main__':
  main() 

