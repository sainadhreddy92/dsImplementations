class solution(object):
  def rangeaddition(self,length,updates):
    res = [0]*(length+1)
    for update in updates:
      res[update[0]]+=update[2]
      res[update[1]+1]-=update[2]
  
    for i in range(1,len(res)):
      res[i]+=res[i-1]

    return res[:length]


def main():
	sol = solution()
	length = 5
    	updates = [
        	[1,  3,  2],
        	[2,  4,  3],
        	[0,  2, -2]]
	print sol.rangeaddition(length,updates)

if __name__=='__main__':
	main()	
