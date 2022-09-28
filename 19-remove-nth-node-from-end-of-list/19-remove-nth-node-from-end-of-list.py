# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        l=0
        
        while current:
            l+=1
            current=current.next
        
        r=root=ListNode()
        i=0
        while head:
            if l-i==n:
                if head:
                    head=head.next
            root.next=head
            
            root=root.next
            if head: head=head.next
            i+=1
        
        return r.next
        