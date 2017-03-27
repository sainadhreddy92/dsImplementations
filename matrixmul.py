import sys

class solution(object):
	def mul(self,matrixA,matrixB):
		rowsA= len(matrixA)
		colsA = len(matrixA[0])
		rowsB = len(matrixB)
		colsB = len(matrixB[0])
	        matrixC =[]	
		if colsA!=rowsB:
			print "Multiplication not possible"
			sys.exit(0)
		for i in range(rowsA):
			level=[]
			for k in range(colsB):
				level.append(0)

			matrixC.append(level)
		rowsC = len(matrixC)
		for i in range(rowsA):
			for j in range(colsB):
                                matrixC[i][j]=0
				for k in range(rowsB):
					matrixC[i][j]+= matrixA[i][k]*matrixB[k][j]
		return matrixC



def main():
	sol = solution()
	matrixA = [[1,2],[3,4]]
	matrixB = [[1,2],[3,4]]
	print sol.mul(matrixA,matrixB)


if __name__=='__main__':
	main()
