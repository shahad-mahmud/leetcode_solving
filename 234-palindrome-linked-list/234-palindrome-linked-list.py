# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sp=fp=head
        
        while(fp and fp.next):
            sp=sp.next
            fp=fp.next.next
        
        # reverse from sp
        prev=None
        while(sp):
            temp=sp.next
            sp.next=prev
            prev=sp
            sp=temp            
        
        while(prev and head):
            if(prev.val!=head.val):
                return False
            prev=prev.next
            head=head.next
        
        return True