from math import sqrt
class solution():
  def findmean(self):
    nums = []
    while True:
      num = raw_input("Enter a number")
      if num=='Y' or num=='N':
        self.calc(nums)
        break
      else:
        if ord(num)>=53 and ord(num)<=57:
          nums.append(int(num))
     

  def calc(self,nums):
    if not nums:
      print "no nums"
      return

    nums.sort()
    if len(nums)%2==1:
      mean= nums[len(nums)/2]

    else:
      mean=(nums[len(nums)/2]+nums[(len(nums)/2)-1])/2

    sd = 0
    tmp = 0
    for num in nums:
      tmp = (num-mean)**2
    
    tmp/=len(nums)
    sd= sqrt(tmp)
    print 'mean is',mean
    print 'sd is',sd



def main():
  solution().findmean()
if __name__=='__main__':
  main()
