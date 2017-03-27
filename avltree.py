class treenode(object):
  def __init__(self,val):
    self.val = val
    self.height= 1
    self.left=None
    self.right=None


class AVLTree(object):
  def getheight(self,root):
    if not root:
      return 0
    else:
      return root.height

  def balance(self,root):
    if not root:
      return 0
    else:
      return self.getheight(root.left)-self.getheight(root.right)

  def rightrotate(self,root):
    x = root.left
    b = x.right
    x.right = root
    root.left = b
    
    root.height= 1+max(self.getheight(root.left),self.getheight(root.right))
    x.height= 1+max(self.getheight(x.left),self.getheight(x.right))

    return x


  def leftrotate(self,root):
    y = root.right
    a = y.left
    
    y.left = root
    root.right = a
  
    root.height= 1+max(self.getheight(root.left),self.getheight(root.right))
    y.height= 1+max(self.getheight(y.left),self.getheight(y.right))
    
    return y

  def insert(self,root,val):
    if not root:
      return treenode(val)

    if val>root.val:
      root.right = self.insert(root.right,val)
    else:
      root.left = self.insert(root.left,val)
   
    root.height = 1+max(self.getheight(root.left),self.getheight(root.right))
    
    bal = self.balance(root)


    if bal>1 and val<root.left.val:
      return self.rightrotate(root)

    if bal>1 and val>root.left.val:
      root.left = self.leftrotate(root.left)
      return self.rightrotate(root)


    if bal<-1 and val>root.right.val:
      return self.leftrotate(root)

    if bal<-1 and val<root.right.val:
      root.right = self.rightrotate(root.right)
      return self.leftrotate(root)

    return root

 



  def inorder(self,root):
    if root:
      print root.val
      self.inorder(root.left)
      self.inorder(root.right)


def main():
  root = None
  root = AVLTree().insert(root,10)
  root = AVLTree().insert(root,20)
  root = AVLTree().insert(root,30)
  root = AVLTree().insert(root,40)
  root = AVLTree().insert(root,50)
  root = AVLTree().insert(root,25)
  AVLTree().inorder(root)



if __name__=='__main__':
  main()


