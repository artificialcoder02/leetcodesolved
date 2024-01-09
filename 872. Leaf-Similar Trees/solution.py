class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        s1 = self.getSequence(root1)
        s2 = self.getSequence(root2)
        if len(s1) != len(s2):
            return False
        return all(a == b for a, b in zip(s1, s2))

    def getSequence(self, root: TreeNode):
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root: TreeNode, result):
        if root is None:
            return
        if root.left is None and root.right is None:
            result.append(root.val)
            return
        self.dfs(root.left, result)
        self.dfs(root.right, result)

