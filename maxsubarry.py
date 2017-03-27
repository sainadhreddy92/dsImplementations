class solution(object):
	def maxsize(self,nums,k):
		dict ={}
		su,i = 0,0
		maxlen = -1
		dict[0]=-1
		while i<len(nums):
			su+=nums[i]
			if not su in dict:
				dict[su]=i
			if su-k in dict:
				maxlen =max(maxlen,i-dict[su-k])
			i+=1
		return maxlen if maxlen>0 else 0




def main():
	sol = solution()
	nums = [1, -1, 5, -2, 3]
	k = 0
	print sol.maxsize(nums,k)


if __name__=='__main__':
	main() 
