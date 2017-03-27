class Solution(object):
  def bestmeetingpoint(self,grid):
    if not grid:
      return -1

    ilist = []
    jlist = []

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j]==1:
          ilist.append(i)
          jlist.append(j)

    jlist.sort()

    d =0
    imed = ilist[len(ilist)/2]
    jmed = jlist[len(jlist)/2]

    for elem in ilist:
      d+=abs(elem-imed)

    for elem in jlist:
      d+=abs(elem-jmed)

    return d 


def main():
  sol = Solution()
  grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]

  print sol.bestmeetingpoint(grid)

if __name__=='__main__':
  main()
