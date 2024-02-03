class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Length of the input array
        n = len(arr)

        # Recursive function to find the maximum sum after partitioning
        def dfs(i):
            # Base case: reached the end of the array
            if i == n:
                return 0

            curMax = curSum = 0

            # Iterate over the next k elements or until the end of the array
            for j in range(i, min(i + k, n)):
                curMax = max(curMax, arr[j])
                
                # Calculate the current sum considering the maximum value in the partition
                cur = curMax * (j - i + 1) + dfs(j + 1)
                
                # Update the current sum if the new one is greater
                curSum = max(curSum, cur)

            return curSum
        return dfs(0)
