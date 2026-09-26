# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        cnt=1
        while curr.next:
            curr=curr.next
            cnt+=1
        cnt = cnt-n
        if cnt == 0:
            return head.next
        curr = head
        prev = None
        while cnt>0 and curr.next:
            prev = curr
            curr=curr.next
            cnt-=1
        prev.next = curr.next
        return head
