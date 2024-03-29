"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        on = {}

        def dfs(node):
            if node in on:
                return on[node]
            
            copy = Node(node.val)
            on[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy 

        return dfs(node) if node else None
