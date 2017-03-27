class TreeNode(object):
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None


class Solution(object):
	def leaves(self,root):
		res =0
		li =[]
		res=self.helper(root,li)
		print li
		return res
	
	def helper(self,root,li):
		if not root:
			return 0
		if root.left==None and root.right==None:
		        li.append(root.val)	
			return 1
		else:
			return self.helper(root.left,li)+self.helper(root.right,li)
	def order(self,root,ord):
		if root:
			self.order(root.left,ord)
			ord.append(root.val)
			self.order(root.right,ord)




	def getleaves(self,root):
		res=[]
		stack=[]
		
		while root or stack:
			while root:
				stack.append(root)
				root=root.left
			root=stack.pop()
			if root.left==None and root.right==None:
				res.append(root.val)
			root = root.right


		return res


	def longestConsecutive(self,root):
		return max(self.dfs(root.left,root.val,1),self.dfs(root.right,root.val,1))


	def dfs(self,root,val,count):
		if root==None:
			return 0
		if root.val-val==1:
			count+=1
		else:	
			count=1

		left_count = self.dfs(root.left,root.val,count)
		right_count = self.dfs(root.right,root.val,count)
		

		return max(left_count,right_count,count)

	

def main():
	root = TreeNode(2)
	root.right = TreeNode(3)
	root.right.left = TreeNode(2)
	root.right.left.left = TreeNode(1)
	sol = Solution()
	print sol.longestConsecutive(root)
	#ord =[]
	#print "Before removal"
	#sol.order(root,ord)
	#print ord
        #print sol.leaves(root)
	#print "After removal"
	#ord=[]
	#sol.order(root,ord)
	#print ord	

if __name__=='__main__':
	main() 
