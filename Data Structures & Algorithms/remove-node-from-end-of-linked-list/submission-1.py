# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, curr = 0 , head
        while curr:
            count += 1
            curr = curr.next
        res = count - n
        if res == 0:
            return head.next
        first = head
        while res > 1:
            res -= 1
            first = first.next
        first.next = first.next.next
        return head
        
        



        