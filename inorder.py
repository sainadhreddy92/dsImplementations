class TreeNode(object):
	def __init__(self,val):
		self.val = val
		self.left=None
		self.right=None




class inorder(object):
	def successor(self,root,p):
		parent = None
		target = None
		while root:
			if root.val==p.val:
				target=root
				break
			elif root.val>p.val:
				parent = root
				root=root.left
			else:
				parent=root
				root=root.right
		print target.val
		print parent.val
		
	
		if target.right:
			target=target.right
			while target.left:
				target=target.left
			return target.val
		
		else:
			return parent.val

				
def main():
	inobj =inorder()
	root = TreeNode(20)
	root.left = TreeNode(8)
	root.right = TreeNode(22)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(12)
	root.left.right.left=TreeNode(10)
	root.left.right.right=TreeNode(14)

	print inobj.successor(root,root.left.right.right)	

if __name__=='__main__':
	main()						
