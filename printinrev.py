class Node():
  def __init__(self,val):
    self.val = val
    self.next = None


class Solution():
  def printinrev(self,root):
    if not root:
      return 

    self.printinrev(root.next)
    print root.val


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  Solution().printinrev(head)

if __name__=='__main__':
  main()
