def oddeven(nums):
  nums.sort(cmp=compare)
  return nums


def compare(num1,num2):
  if num1%2==1 and num2%2==1:
    if num1>num2:
       return -1
    elif num1<num2:
       return 1
    else:
       return 0

  elif num1%2==0 and num2%2==0:
    if num1>num2:
       return 1
    elif num1<num2:
       return -1
    else: 
       return 0
  else:
    if num1%2==1:
      return -1
    else:
      return 1


def main():
  nums = [1, 2, 3, 5, 4, 7, 10]
  print oddeven(nums)


if __name__=='__main__':
  main()
