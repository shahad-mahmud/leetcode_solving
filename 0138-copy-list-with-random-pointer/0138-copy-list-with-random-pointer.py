"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        new_nodes = {None: None}
        
        current = head
        
        while current:
            new_node = Node(current.val)
            new_nodes[current] = new_node
            
            current = current.next
        
        current = head
        while current:
            new_nodes[current].next = new_nodes[current.next]
            new_nodes[current].random = new_nodes[current.random]
            
            current = current.next
        
        return new_nodes[head]
        
        
        