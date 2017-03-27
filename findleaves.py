class solution():
  def findleaves(self,root):
    res =[]
    if not root:
      return res
    self.helper(res,root)
    return res

  def helper(self,res,root):
    if not root:
      return -1

    left = self.helper(res,root.left)
    right = self.helper(res,root.right)
    level = max(left,right)+1
 
    if len(res)==level:
      res.append([])
 
    res[level].append(root.val)

    return level

class TreeNode():
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None


def main():
  root = TreeNode(1)
  root.left=TreeNode(2)
  root.right=TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  print solution().findleaves(root)

if __name__=='__main__':
  main()
