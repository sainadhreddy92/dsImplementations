class Solution(object):
  def wallsandgates(self,input):
    if not input:
      return
    for i in range(len(input)):
      for j in range(len(input[0])):
        if input[i][j]==0:
          self.update(input,i+1,j,1)
          self.update(input,i,j+1,1)
          self.update(input,i-1,j,1)
          self.update(input,i,j-1,1)

  def update(self,input,i,j,val):
    if i<len(input) and j<len(input) and i>=0 and j>=0 and input[i][j]!=-1 and input[i][j]!=0 and input[i][j]>val:
      input[i][j]=val
      self.update(input,i+1,j,val+1)
      self.update(input,i,j+1,val+1)
      self.update(input,i-1,j,val+1)
      self.update(input,i,j-1,val+1)

  def walls2(self,input):
    if not input:
      return
    queue = []
    for i in range(len(input)):
      for j in range(len(input[0])):
        if input[i][j]==0:
          queue.append((i,j))
    while queue:
      elem = queue.pop(0)
      r = elem[0]
      c = elem[1]
      print "here"
      if r+1<len(input) and input[r+1][c]==2**31-1:
        input[r+1][c]=input[r][c]+1
        queue.append((r+1,c))

      if r-1>=0 and input[r-1][c]==2**31-1:
        input[r-1][c]=input[r][c]+1
        queue.append((r-1,c))

      if c+1<len(input[0]) and input[r][c+1]==2**31-1:
        input[r][c+1]=input[r][c]+1
        queue.append((r,c+1))

      if c-1>=0 and input[r][c-1]==2**31-1:
        input[r][c-1]=input[r][c]+1
        queue.append((r,c-1))

def main():
  input = [[2**31-1,-1,0,2**31-1],[2**31-1,2**31-1,2**31-1,-1],[2**31-1,-1,2**31-1,-1],[0,-1,2**31-1,2**31-1]]
  print input
  #Solution().wallsandgates(input)
  Solution().walls2(input)
  print input

if __name__=='__main__':
  main()
