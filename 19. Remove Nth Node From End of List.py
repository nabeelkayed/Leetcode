# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
    
        l = head
        length = 1
        while l.next != None:
            length += 1
            l = l.next
        nIndex = length - n


        p = head
        c = head.next
        count = 1
        if nIndex == 0:
            head = head.next
        while count < nIndex:
            if c.next == None:
                break
            c = c.next
            p = p.next
            count = count +1
        p.next = c.next
        return head
