class Node():
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

def buildtree(inorder,pre,instart,inend):
  if instart>inend:
    return None
  node = Node(pre[buildtree.preindex])
 
  buildtree.preindex+=1
 
  if instart==inend:
    return node
 
  inindex = search(inorder,node.data,instart,inend)

  node.left = buildtree(inorder,pre,instart,inindex-1)
  node.right = buildtree(inorder,pre,inindex+1, inend)

  return node

def search(inorder,char,instart,inend):
  
  for i in range(instart,inend+1):
    if char == inorder[i]:
      return i

def inorder_trave(root):
  res = []
  helper(res,root)
  return res

def helper(res,root):
  if root:
    helper(res,root.left)
    res.append(root.data)
    helper(res,root.right)


def main():
  inorder = ['D','B','E','A','F','C']
  pre = ['A','B','D','E','C','F']
  
  buildtree.preindex = 0
  root = buildtree(inorder,pre,0,5)

  print root.data
  print root.left.data
  print root.right.data

  print inorder_trave(root)


if __name__=='__main__':
  main()
