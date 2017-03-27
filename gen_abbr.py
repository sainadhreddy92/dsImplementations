class solution(object):
	def abbr(self,word):
		res =[]
		size = 2**len(word)
		i=0
		while i<size:
			j=0
			s = ''
			count = 0
			temp =i
			while j<len(word):
				if temp&1:
					count+=1
					j+=1
					if j==len(word):
						s=s+str(count)
				else:
					if count:
						s=s+str(count)
						count=0
					s=s+word[j]
					j+=1
				temp=temp>>1
			res.append(s)
			i+=1

		return res
		
def main():
	sol = solution()
	word = 'ab'
	res = sol.abbr(word)
	for re in res:
		print re


if __name__=='__main__':
	main()

