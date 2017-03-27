class Solution(object):
  dict ={}
  def logger(self,timestamp,message):
    if self.dict and message in self.dict:
      print timestamp
      print self.dict[message]
      if abs(self.dict[message]-timestamp)>=10:
        self.dict[message]=timestamp
        return True
      else:
        self.dict[message]=timestamp
        return False
    else:
      self.dict[message]=timestamp
      return True

def main():
  sol = Solution()
  print sol.logger(1,"foo")
  print sol.logger(2,"bar")
  print sol.logger(3,"foo")
  print sol.logger(8,"bar")
  print sol.logger(10,"foo")
  print sol.logger(11,"foo")


if __name__=='__main__':
  main()
