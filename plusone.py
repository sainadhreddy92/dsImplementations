class solution(object):
  def plusone(self,head):
    if not head:
      return head
  
    head = newhead = self.rev(head)

    first = 1
    carry = 0
    while head:
      if first:
        if head.val==9:
          head.val=0
          carry = 1
        else:
          head.val+=1
        first = 0
      else:
        if carry:
          if head.val==9:
            head.val=0
            carry = 1
          else:
            head.val+=1
            carry = 0
      head = head.next
    dummy = ListNode(1)
    dummy.next = self.rev(newhead)
    if carry:
      return dummy
    return dummy.next

  def rev(self,head):
    if not head:
      return head
    
    curr = head
    prev = None

    while curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
   
    return prev

  def traverse(self,head):
    while head:
      print head.val
      head = head.next


  def plusone2(self,head):
    if not head:
      return head

    carry = self.helper(head)
    if carry:
      newnode = ListNode(1)
      newnode.next = head
      head = newnode
    return head



  def helper(self,head):
    if not head:
      return -1

    carry = self.helper(head.next)

    if carry==-1 or carry==1:
      if head.val==9:
        head.val=0
        caryy=1
      else:
        head.val+=1
        carry = 0
    return carry


  def plusone3(self,head):
    if not head:
      return head
    dummy = ListNode(0)
    dummy.next = head
    lastnot9 = dummy

    while head:
      if head.val!=9:
        lastnot9=head
      head=head.next

    lastnot9.val+=1
    next = lastnot9.next
    while next:
      next.val = 0
      next = next.next

    if dummy.val==1:
      return dummy
    return dummy.next

class ListNode():
  def __init__(self,x):
    self.val = x
    self.next = None

def main():
  sol = solution()

  head = ListNode(9)
  #head.next = ListNode(9)
  #head.next.next = ListNode(9)
  head = sol.plusone3(head)
  sol.traverse(head)

if __name__=='__main__':
  main()
