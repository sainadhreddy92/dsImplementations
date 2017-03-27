class bst():
  def __init__(self,tup):
    self.tuple = tup
    self.left = None
    self.right = None

def inorder(root):
  res = []
  helper(root,res)  
  print res

def helper(root,res):
  if root:
    helper(root.left,res)
    res.append(root.tuple[0])
    helper(root.right,res)

def insert(root,tup):
  if not root:
    root=bst(tup)
  elif tuple_compare(root.tuple,tup)==1:
    root.left= insert(root.left,tup)
  else:
    root.right = insert(root.right,tup)
  
  return root


def tuple_compare(tup1,tup2):
  if tup1[0]>tup2[0]:
    return 1
  elif tup1[0]<tup2[0]:
    return -1
  else:
    return 0


def main():
  tups = [ (1,10),(2,20),(3,30),(4,40),(5,50)]
  root = bst((3,30))
  root.left = bst((2,20))
  root.right = bst((4,40))
  root = insert(root,(1,10))
  root = insert(root,(5,50))
  inorder(root)

if __name__=='__main__':
  main()
