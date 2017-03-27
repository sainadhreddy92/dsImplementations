class solution():
  def sample(self,A):
    A.append("hello")

  def torf(self):
    return True

def main():
  array = ["hi","how","are","you"] #array initialization
  solution().sample(array)
  #print array
  print solution().torf

if __name__=="__main__":
  main()
