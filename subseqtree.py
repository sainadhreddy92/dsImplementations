class TreeNode(object):
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right=None


class sol(object):
  def longsubsequence(self,root):
    if not root:
      return 0
    return max(self.helper(root.right,1,root.val+1),self.helper(root.left,1,root.val+1))

  def helper(self,root,curr,val):
    if not root:
      return curr
    if root.val==val:
      curr+=1
    else:
      curr=1
    
    return max(curr,self.helper(root.left,curr,root.val+1),self.helper(root.right,curr,root.val+1))   


  def order(self,root,ord):
    if root:
      self.order(root.left,ord)
      ord.append(root.val)
      self.order(root.right,ord)

def main():
  s=sol()
  root=TreeNode(1)
  root.right=TreeNode(3)
  root.right.left=TreeNode(2)
  root.right.right=TreeNode(4)
  root.right.right.right=TreeNode(5)
  
  print s.longsubsequence(root)

if __name__=='__main__':
  main()
