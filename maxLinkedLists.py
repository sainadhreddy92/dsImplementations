def maxsumlinkedlists(l1,l2):
  if not l1:
    return l2

  if not l2:
    return l1

  dummy = ListNode(0)
  dummy2=dummy


  while l1 or l2:
    sum1 = 0
    sum2 = 0
    
    l1start = l1
    l2start = l2
    while l1 and l2 and l1.val!=l2.val:
      if l1.val<l2.val:
        sum1+=l1.val
        l1 = l1.next
      else:
        sum2+=l2.val
        l2 = l2.next

    if not l2:
      while l1:
        sum1+=l1.val
        l1 = l1.next


    if not l1:
      while l2:
        sum2+=l2.val
        l2=l2.next
    if sum1>sum2:
      dummy.next = l1start
      dummy = dummy.next
      if l1 and l1==l1start:
        l1 = l1.next
      if l2 and l2==l2start:
        l2 = l2.next
      while dummy and dummy.next!=l1:
        dummy = dummy.next
    elif sum1<sum2:
      dummy.next = l2start
      dummy = dummy.next
      if l1 and l1==l1start:
        l1 = l1.next
      if l2 and l2==l2start:
        l2 = l2.next
      while dummy and dummy.next!=l2:
        dummy = dummy.next
    else:
      dummy.next = l2start
      dummy = dummy.next
      l1 = l1.next
      l2=l2.next
      while dummy and dummy.next!=l2:
        dummy = dummy.next



 

  return dummy2.next


def traverse(head):
  while head:
    print head.val
    head = head.next

def main():
  l1 = ListNode(1)
  l1.next = ListNode(3)
  l1.next.next = ListNode(30)
  l1.next.next.next = ListNode(90)
  l1.next.next.next.next = ListNode(120)
  l1.next.next.next.next.next = ListNode(240)
  l1.next.next.next.next.next.next = ListNode(511)

  l2 = ListNode(0)
  l2.next = ListNode(20)
  l2.next.next = ListNode(40)
  l2.next.next.next = ListNode(50)
  l2.next.next.next.next = ListNode(60)
  l2.next.next.next.next.next = ListNode(1000)
  
  newnode = maxsumlinkedlists(l1,l2)
  traverse(newnode)

class ListNode():
  def __init__(self,val):
    self.val = val
    self.next = None

if __name__=='__main__':
  main()
