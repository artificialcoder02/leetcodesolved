class Solution(object):
    def __init__(self):
        self.result = 0

    def averageOfSubtree(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return [0, 0]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        currentSum = left[0] + right[0] + node.val
        currentCount = left[1] + right[1] + 1

        if currentSum // currentCount == node.val:
            self.result += 1

        return [currentSum, currentCount]
        
