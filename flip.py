def flip(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  for i in range(0,rows):
    for j in range(cols-i):
      if i!=j:
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
  return matrix

def main():
  matrix =[[1,2,3],[4,5,6],[7,8,9]]
  print matrix
  print flip(matrix)
if __name__=='__main__':
  main()
