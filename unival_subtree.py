class Solution(object):
  def univaltree(self,root):
    count = [0]
    self.helper(root,count)
    return count[0]


  def helper(self,root,count):
    if not root:
      return True
    
    left = self.helper(root.left,count)
    right = self.helper(root.right,count)

    if left and right:
      
      if root.left and root.val!=root.left.val:
        return False

      if root.right and root.val!=root.right.val:
        return False
      
      count[0]+=1
      return True
    return False


class TreeNode(object):
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None


def main():
  root = TreeNode(5)
  root.left = TreeNode(1)
  root.right = TreeNode(5)
  root.left.left = TreeNode(5)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(5)

  print Solution().univaltree(root)

if __name__=='__main__':
  main()
