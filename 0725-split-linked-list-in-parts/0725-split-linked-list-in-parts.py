# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        curr = head
        res = []
        while k:
            taken = 1
            part_len = math.ceil(max(1, l/k))
            
            new_head = curr
            while taken < part_len and curr:
                curr = curr.next
                taken += 1
            
            if curr:
                nxt = curr.next
                curr.next = None
            
                curr = nxt
            
            res.append(new_head)
            l -= part_len
            k -= 1
        
        return res
        