class solution(object):
  def findperm(self,seq):
    res = [0]*(len(seq)+1)

    for i in range(len(res)):
      res[i]=i+1

    i = 0
    while i<len(seq):
      low = i
      if seq[i]=='D':
        while i<len(seq) and seq[i]=='D':
          i+=1
          high=i
        self.rev(res,low,high)
      i+=1
    return res


  def rev(self,nums,low,high):
    while low<high:
      nums[low],nums[high]=nums[high],nums[low]
      low+=1
      high-=1


def main():
  seq = 'D'
  print solution().findperm(seq)


if __name__=='__main__':
  main()
