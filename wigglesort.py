class solution(object):
	def wigglesort(self,nums):
		i=1
		while i<len(nums):
			if (i%2==0 and nums[i]<=nums[i-1]) or (i%2==1 and nums[i]>=nums[i-1]):
				i+=1
				continue
			else:
				temp = nums[i-1]
				nums[i-1]=nums[i]
				nums[i] = temp
				i+=1
		print nums



def main():
	sol = solution()
	nums = [3, 5, 2, 1, 6, 4]	
	print nums
	sol.wigglesort(nums)

if __name__=='__main__':
	main()



