class solution():
  def smallest(self,grid,x,y):
    if not grid or x<0 or y<0 and x>=len(grid) or y>=len(grid[0]):
      return True
    m = len(grid)
    n = len(grid[0])

    left = self.searchcols(grid,0,y,0,m,True)
    right = self.searchcols(grid,y,n-1,0,m,False)
    top = self.searchrows(grid,0,x,0,n,True)
    bottom = self.searchrows(grid,x,m-1,0,n,False)
    
    print left,right,top,bottom

    return (right-left)*(bottom-top)



  def searchcols(self,grid,i,j,top,bottom,goleft):
    while i!=j:
      k=top
      mid = (i+j)/2
      while k<bottom and grid[k][mid]==0:
        k+=1
      if k<bottom and goleft:
        j=mid
      else:
        i=mid+1

    return i



  def searchrows(self,grid,i,j,left,right,gotop):
    while i!=j:
      k = left
      mid = (i+j)/2
      while k<right and grid[mid][k]==0:
        k+=1
      if k<right and gotop:
        j=mid
      else:
        i=mid+1


    return i


def main():
  grid=[[0,0,0,0],[0,0,1,0],[0,1,1,0],[0,0,0,0]]

  print  solution().smallest(grid,2,2)

if __name__=='__main__':
  main()
