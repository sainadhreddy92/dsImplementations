import sys
class solution(object):
  def wallsandgates(self,matr):
    li=[]
    if not matr:
      return matr
    m = len(matr)
    n = len(matr[0])


    for i in range(m):
      for j in range(n):
        if matr[i][j]==0:
          li.append((i,j))

    while (li):
      (row,col)  = li.pop(0)

      if (0<=row-1<m and matr[row-1][col]==sys.maxint):
        matr[row-1][col]=(matr[row][col])+1
        li.append((row-1,col))

      if (0<=row+1<m and matr[row+1][col]==sys.maxint):
        matr[row+1][col]=(matr[row][col])+1
        li.append((row+1,col))

      if (0<=col-1<n and matr[row][col-1]==sys.maxint):
        matr[row][col-1]=(matr[row][col])+1
        li.append((row,col-1))

      if (0<=col+1<n and matr[row][col+1]==sys.maxint):
        matr[row][col+1]=(matr[row][col])+1
        li.append((row,col+1))


    for i in range(m):
      print matr[i]


def main():
  matr = [[sys.maxint,-1,0,sys.maxint],[sys.maxint,sys.maxint,sys.maxint,-1],[sys.maxint,-1,sys.maxint,-1],[0,-1,sys.maxint,sys.maxint]]
  sol = solution()
  sol.wallsandgates(matr)


if __name__=='__main__':
  main()
