class solution(object):
	def largenumber(self,nums):
		comp = lambda a,b:1 if a+b>b+a else -1 if a+b<b+a else 0
		nums = map(str,nums)
		nums.sort(cmp=comp,reverse=True)
 		return ''.join(nums)



def main():
	sol = solution()
        nums = [3, 30, 34, 5, 9]
        print sol.largenumber(nums)


if __name__=='__main__':
	main()	
