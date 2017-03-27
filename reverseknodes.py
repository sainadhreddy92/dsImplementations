class solution(object):
	def reverselast(self,root,k):
		length=0
		if k==0:
			return root
		else:
			dummy = root
			head = root
			while dummy:
				length+=1
				dummy=dummy.next

			for i in range(length-k-1):
				head = head.next
			head.next = self.reverselist(head.next)
		return root

	def reverselist(self,root):
		if not root:
			return root
		prev,curr,next = None,root,None
		
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		return prev
	
	def traverse(self,root):
		res =[]
		
		while root:
			res.append(root.val)
			root = root.next

		return res

class Node(object):
	def __init__(self,val):
		self.val = val
		self.next = None


def main():
	sol = solution()
	root = Node(1)
	root.next = Node(2)
	root.next.next = Node(3)
	root.next.next.next = Node(4)
	root = sol.reverselast(root,1)
	print sol.traverse(root)

if __name__=='__main__':
	main()
	
	
