class solution(object):
	def plusone(self,root):
		root = self.rever(root)
		carry = 0
		first = 1
		curr = root
		prev = None
		while curr:
			if first:
				curr.val+=carry+1
				first =0
			else:
				curr.val+=carry
			
			carry = 0
			if curr.val>9:
				curr.val-=10
				carry = 1
			prev = curr
			curr=curr.next
		if carry:
			new = Node(carry)
			prev.next = new
		root = self.rever(root)
		return root

	
	
	def rever(self,root):
		if not root:
			return None
		prev = next=None
		curr = root

		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		return prev
	
	def traverse(self,root):
		res=[]
		while root:
			res.append(root.val)
			root=root.next
		return res

class Node(object):
	def __init__(self,val):
		self.val = val
		self.next = None
	


def main():
	root = Node(0)
	#root.next = Node(9)
	#root.next.next = Node(9)
	sol = solution()
	print sol.traverse(root)
	root = sol.plusone(root)
	print sol.traverse(root)

if __name__=='__main__':
	main()

	
