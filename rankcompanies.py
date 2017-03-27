class solution(object):
	def rankcompanies(self,dict):
		return sorted(dict.items(), key=lambda x:x[1])


def main():
	sol = solution()
	dict = {'Oracle':25,'Google':1,'Apple':22,'Amazon':89,'Juniper':200,'Cisco':55}
	print sol.rankcompanies(dict)


if __name__=='__main__':
	main()
