class solution(object):
	def sortarray(self,nums,a,b,c):
		nums=map(lambda x: a*(x**2)+(b*x)+c,nums)
		return sorted(nums)

def main():
	nums = [-4, -2, 2, 4]
	sol = solution()
	a,b,c =1,3,5
	print sol.sortarray(nums,a,b,c)


if __name__=='__main__':
	main()
