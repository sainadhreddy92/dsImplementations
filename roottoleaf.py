class treenode(object):
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class solution(object):
  def leafs(self,root):
    res =[]
    vals=[]
    self.helper(root,res,vals)
    return res

  def helper(self,root,res,vals):
    if root.left==None and root.right==None:
      vals.append(root.val)
      res.append(vals)
    if root.left:
      self.helper(root.left,res,vals+[root.val])
    if root.right:
      self.helper(root.right,res,vals+[root.val])

def main():
  sol = solution()
  root = treenode(1)
  root.left=treenode(2)
  root.right=treenode(3)
  root.left.left = treenode(4)
  root.left.right = treenode(5)
  root.right.left = treenode(6)
  root.right.right = treenode(7) 
  print sol.leafs(root)

if __name__=='__main__':
  main()
