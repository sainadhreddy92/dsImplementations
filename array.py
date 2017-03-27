def array(nums,size):
  i = 0
  grid =[]
  for _ in range(size):
    le =[]
    print i
    for j in range(size):
      #print i+j
      le.append(nums[i+j])
      grid.append(le)
    i+=4
  print grid

def main():
  nums = '3 0 0 0 0 3 3 0 0 1 0 3 0 2 3 3'.strip().split()
  nums = map(int,nums)
  array(nums,4)



if __name__=='__main__':
  main()
  
