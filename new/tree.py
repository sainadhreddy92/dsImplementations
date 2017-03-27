class TreeNode(object):
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class Solution(object):
  count=0
  def getleaves(self,root):
    res = []
    if not root:
      return res
    self.helper(root,res)
    return res

  def helper(self,root,res):
    if not root:
      return
    if root.left==None and root.right==None:
      res.append(root.val)
      return
    self.helper(root.left,res)
    self.helper(root.right,res)

  def getleaves2(self,root):
    if not root:
      return []
    res =[]
    stack = [root]

    while stack:
      for _ in range(len(stack)):
        node = stack.pop(0)

        if node.left==None and node.right==None:
          res.append(node.val)

        if node.left:
          stack.append(node.left)

        if node.right:
          stack.append(node.right)
    return res

  def findsecond(self,root,c):
    if not root or c>=2:
      return

    self.findsecond(root.right,c)

    c+=1

    if c==2:
      print root.val
      return root.val

    self.findsecond(root.left,c)


  def verticaltraversal(self,root):
    level_dict ={}
    if not root:
      return []
    nodes =[root]
    levels =[0]
    min_level = 2**31-1
    max_level =-min_level-1
    while nodes:

      node = nodes.pop(0)
      level = levels.pop(0)
      if level in level_dict:
        level_dict[level].append(node.val)
      else:
        level_dict[level]=[node.val]

      if node.left:
        nodes.append(node.left)
        levels.append(level-1)
        min_level = min(min_level,level-1)

      if node.right:
        nodes.append(node.right)
        levels.append(level+1)
        max_level = max(max_level,level+1)
    print level_dict
    res=[]
    i=min_level
    while i<=max_level:
      res.append(level_dict[i])
      i+=1
    return res


def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(7)
  print Solution().verticaltraversal(root)


if __name__=='__main__':
  main()
