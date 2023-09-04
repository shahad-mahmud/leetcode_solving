# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = head
        sp = head
        
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            
            if sp == fp:
                return True
        
        return False
        