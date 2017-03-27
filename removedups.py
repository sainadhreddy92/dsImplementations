#using python 2
#the main point is to illustrate by example
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def nthelementfromlast(self,head,n):
        if not head:
            return None
        p1 = p2 = head
        while head and n>=0:
            
    def removedups(self,head):
        if not head:
            return head
        node_map = {}
        prev = None
        curr = head
        while  curr:
            if curr.val in node_map:
                prev.next = curr.next
            else:
                node_map[curr.val]=1
                prev = curr

            curr = curr.next

        return head


    def traversal(self,head):
        if not head:
            return
        while head:
            print head.val
            head  = head.next

def main():
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(1)
    Solution().traversal(head)
    head = Solution().removedups(head)
    print "After removing dups"
    Solution().traversal(head)



if __name__=='__main__':
    main()
