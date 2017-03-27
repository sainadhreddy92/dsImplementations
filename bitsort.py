class solution(object):
  def bitsort(self,bitmap,maxlength):
    res =[]
    for num in range(maxlength+1):
      if bitmethods(5).checkval(num,bitmap):
        res.append(num)
    return res

class bitmethods(object):
  def __init__(self,bits):
    self.bits=bits
    self.mask = 0x1F

  def set(self,index,bitmap):
    bitmap[index>>self.bits] |= (1 << (index & self.mask))
    return bitmap

  def clear(self,index,bitmap):
    bitmap[index>>self.bits] &= ~(1 << (index & self.mask))
    return bitmap

  def checkval(self,index,bitmap):
    return bitmap[index>>self.bits] & (1 << (index & self.mask))


def main():
  sol = solution()
  arr=[33,10,18,22,2,4,19,7,7,26,27]
  bitm = bitmethods(5)
  bitmap =[]
  for i in range(1+33/32):
      bitmap.append(0)
  for num in arr:
    bitmap = bitm.set(num,bitmap)
  
  print arr 
  print sol.bitsort(bitmap,33)


if __name__=='__main__':
  main()
