class Node(object):
  def __init__(self,val):
    self.val = val
    self.next = None


class Solution(object):
  def traverse(self,head):
    while head:
      print head.val
      head = head.next

  def reverselist(self,head):
    prev = None
    curr = head
    
    while curr:
      nex = curr.next
      curr.next = prev
      prev = curr
      curr = nex
    return prev


  def reverselist2(self,head,prev):
    if not head:
      return prev

    next = head.next

    head.next = prev

    return self.reverselist2(next,head)
    
    

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)

  sol = Solution()

  sol.traverse(head)

  print "Reveresed"

  head = sol.reverselist2(head,None)

  sol.traverse(head)

if __name__=='__main__':
  main()
