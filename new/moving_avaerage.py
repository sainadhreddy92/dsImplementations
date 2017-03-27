class movingAverage(object):
  def __init__(self,size):
    self.queue = []
    self.size = size
    self.su = 0

  def next(self,val):
    if len(self.queue)<self.size:
      self.queue.append(val)
      self.su+=val
    else:
      popped_val = self.queue.pop(0)
      self.su-=popped_val
      self.queue.append(val)
      self.su+=val
    return self.su/(len(self.queue)*1.0)


def main():
  move = movingAverage(3)
  print move.next(1)
  print move.next(10)
  print move.next(3)
  print move.next(5)


if __name__=='__main__':
  main()      
