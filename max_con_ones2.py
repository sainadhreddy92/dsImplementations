class Solution(object):
  def max_con_ones(self,input):
    max_ones = zero_count = one_count = 0
    
    for element in input:
      if element == 1:
        one_count+=1
      else:
        zero_count+=1
        if zero_count==2:
          zero_count=0
          max_ones = max(max_ones,one_count)
          one_count = 0
        elif zero_count==1:
          one_count+=1

    return max_ones

def main():
  input = [1,0,1,1,1,0,0]
  print Solution().max_con_ones(input)

if __name__=='__main__':
  main()
