def swapnodes(head):
  if not head or not head.next:
    return head


  dummy = TreeNode(0)
  newhead = dummy
  

  while head and head.next:
    dummy.next = head.next
    next = head.next.next
    head.next.next = head
    dummy = head
    head.next = next
    head = next

  return newhead.next


def traverse(head):
  while head:
    print head.val
    head = head.next

class TreeNode():
  def __init__(self,val):
    self.val = val
    self.next = None

def main():
  head = TreeNode(1)
  head.next = TreeNode(2)
  head.next.next = TreeNode(3)
  head.next.next.next = TreeNode(4)
  traverse(head)
  head = swapnodes(head)
  traverse(head)


if __name__=='__main__':
  main()
