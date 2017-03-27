class Solution(object):
  def closest(self,root,target):
    ret = root.val
    while root!=None:
      if abs(root.val-target)<abs(ret-target):
        ret = root.val
      if target>root.val:
        root=root.right
      else:
        root=root.left
    return root


