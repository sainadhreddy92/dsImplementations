class solution(object):
	def twosum(self,nums,target):
		i=0
		index=[]
		while i < len(nums):
			index = self.bsearch(nums,target-nums[i])
			if index and index!=i:
				li=[index]+[i]
				return sorted(li)
			else:
				i+=1
		

	def bsearch(self,nums,target):
		left = 0
		right = len(nums)-1
		while left<right:
			mid = left+(right-left)//2
			if nums[mid]==target:
				return mid
			elif target>nums[mid]:
				left = mid+1
			else:
				right = mid-1


def main():
	sol = solution()
	nums = [1,2,3,4]
	print sol.twosum(nums,7)	


if __name__=='__main__':
	main()	
