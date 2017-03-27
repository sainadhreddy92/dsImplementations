class solution():
  res =[]
  def zigzag(self,vector1,vector2):
    l1 = len(vector1)
    l2 = len(vector2)
    length = max(l1,l2)
   
    for i in range(length):
      if i< l1:
	self.res.append(vector1[i])
      if i<l2:
        self.res.append(vector2[i])
 
  def hasNext(self):
    if len(self.res)>0:
      return True
    else:
      return False

  def next(self):
    return self.res.pop(0)



def main():
  sol = solution()
  v1 = [1,2]
  v2 = [3,4,5,6]
  sol.zigzag(v1,v2)
  
  for i in range(len(v1)+len(v2)):
    if sol.hasNext():
      print sol.next()


if __name__=='__main__':
  main()
