import random
from globals import * 

class graphs():
  def CalcRowsum(self,weight,row):
    rowsum =0
    for i in range(len(weight[row])):
      if weight[row][i]!=0:
        rowsum+=1
    return rowsum

  def CalcColsum(self,weight,col):
    colsum =0
    for i in range(len(weight)):
      if weight[i][col]!=0:
        colsum+=1
    return colsum


  def print_weight(self,weight):
    for i in range(globals().vertices):
      print self.CalcRowsum(weight,i)  
    #print le


  def random_generate2(self,weight):
    for i in range(globals().vertices):
      tried=0
      rsum = self.CalcRowsum(weight,i)
      while rsum<globals().degree2:
        tried+=1
        j = random.randint(0,globals().vertices-1)
        if self.CalcColsum(weight,j)<globals().WEIGHTRANGE  and j!=i and weight[i][j]==0:
          weight[i][j]= weight[j][i] = random.randint(0,globals().WEIGHTRANGE)
          rsum+=1
        if tried>=globals().vertices:
          i=-1
          break
    return weight

  def random_generate(self,weight):
    for i in range(globals().vertices):
      tried=0
      rsum = self.CalcRowsum(weight,i)
      while rsum<globals().degree1:
        tried+=1
        j = random.randint(0,globals().vertices)
        if self.CalcColsum(weight,j)<globals().degree2 and j!=i and weight[i][j]==0:
          weight[i][j]= weight[j][i] = random.randint(0,lobal().WEIGHTRANGE)
          rsum+=1
        if tried>=globals().vertices:
          i=-1
          break
    return weight

  def initialize(self,weight):
   for i in range(globals().vertices):
    for j in range(globals().vertices):
      weight[i][j]=0
   return weight

def main():
  weight_matrix=[]
  for i in range(50):
    le = []
    for j in range(50):
      le.append(0)
    weight_matrix.append(le)
  g = graphs()
  k =0
  while k<50:
    while (g.CalcRowsum(weight_matrix,k)!=10):
      weight_matrix = g.initialize(weight_matrix)
      k=0
      weight_matrix = g.random_generate2(weight_matrix)
    k+=1
  print "yes"
  g.print_weight(weight_matrix)

if __name__=='__main__':
  main()
