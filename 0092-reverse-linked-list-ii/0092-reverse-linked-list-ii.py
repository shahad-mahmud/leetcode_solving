# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        self.i = 1
        
        def reverse(head):
            prev = None            
            c = head
            
            while c:
                if self.i > right:
                    break
                
                temp = c.next
                c.next = prev
                prev = c
                c = temp
                
                self.i += 1
            

            head.next = c
            
            return prev
        
        
        c = head
        l_prev = None
        while c:
            if self.i == left:
                rev = reverse(c)
                if l_prev:
                    l_prev.next = rev
                    break
                else:
                    return rev
                
            
            l_prev = c
            c = c.next
            self.i += 1
        
        return head