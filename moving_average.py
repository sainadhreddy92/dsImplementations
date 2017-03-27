import sys

class MovingAverage(object):
  sum = 0
  queue=[]
  def __init__(self,size):
    self.size=size
    

  def next(self,num):
    if len(self.queue)>=self.size:
      self.sum = self.sum-self.queue[0]
      self.queue.pop(0)
    self.sum = self.sum+num
    self.queue.append(num)
    return self.sum/(len(self.queue)*1.0)


def main():
  mv = MovingAverage(3)
  print mv.next(1)
  print mv.next(10)
  print mv.next(3)
  print mv.next(5)

if __name__=='__main__':
  main()
