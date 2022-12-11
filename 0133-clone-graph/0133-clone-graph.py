"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        nodes = {}
        visited = set()
        
        def dfs(head):
            if not head or head.val in visited: return
            
            node = Node(head.val)
            nodes[head.val] = node
            visited.add(head.val)
            
            for child in head.neighbors:
                dfs(child)
        
        dfs(node)
        
        visited = set()
        def copy(head):
            if not head or head.val in visited: return
            visited.add(head.val)
            
            for child in head.neighbors:
                nodes[head.val].neighbors.append(nodes[child.val])
                copy(child)
        
        copy(node)
        return nodes[node.val]
            