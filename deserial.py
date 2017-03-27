class solution():
  def serialize(self,root):
    res = ''
    if not root:
      return '#,'
    
    res+=str(root.val)+','
    res+=self.serialize(root.left)
    res+=self.serialize(root.right)

    return res


  def deserialize(self,ser):
    if not ser:
      return
    serlist = ser.split(',')
    return self.helper(serlist)


  def helper(self,serlist):
    if not serlist:
      return None
    popelem = serlist.pop(0)
    if popelem == '#':
      return None

    root = TreeNode(popelem)
    root.left = self.helper(serlist)
    root.right = self.helper(serlist)

    return root

  def inorder(self,root):
    res = []
    self.helper2(root,res)
    return res

  def helper2(self,root,res):
    if not root:
      return
    
    self.helper2(root.left,res)
    res.append(root.val)
    self.helper2(root.right,res)
  

class TreeNode():
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None



def main():
  root = TreeNode(10)
  root.left = TreeNode(8)
  root.right = TreeNode(16)
  root.left.left = TreeNode(6)
  root.left.right = TreeNode(5)
  root.right.left = TreeNode(11)
  root.right.right = TreeNode(17)
  print solution().inorder(root)
  ser = solution().serialize(root)
  print ser
  root2 = solution().deserialize(ser)
  print solution().inorder(root2)

if __name__=='__main__':
  main()
