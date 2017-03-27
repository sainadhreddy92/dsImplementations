class solution(object):
	def meeting_rooms(self,nums):
		starts=[]
		ends =[]
		rooms =0
		for num in nums:
			starts.append(num[0])
			ends.append(num[1])
		starts.sort()
		ends.sort()

		i=j=0

		while i<len(starts):
			if starts[i]<ends[j]:
				rooms+=1
			else:
				j+=1
			i+=1
		return rooms	



def main():
	nums = [[0, 30],[5, 10],[15, 20]]
	sol = solution()
	print sol.meeting_rooms(nums)


if __name__=='__main__':
	main()
		
