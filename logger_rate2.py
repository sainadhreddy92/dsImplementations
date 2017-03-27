class solution(object):
  self.queue = []
  self.messages = set()
  def loggerrate(self,timestamp,message):
    while self.queue and timestamp-self.queue[0][0]>=10:
      (stamp,mes) = self.queue.pop(0)
      self.messages.remove(mes)
  
    if message in self.messages:
      self.queue.append((timestamp,message))
      return False
    else:
      self.queue.append((timestamp,message))
      self.messages.add(message)
      return True

def main():
  
