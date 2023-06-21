class Solution:
    def helper(self, nums, cost, all):
        total_cost = 0
        for i in range(len(nums)):
            total_cost += abs(nums[i] - all) * cost[i]
        return total_cost

    def minCost(self, nums, cost):
        left = nums[0]
        right = nums[0]
        for i in nums:
            left = min(left, i)
            right = max(right, i)
        ans = 0
        while left < right:
            mid = (left + right) // 2
            cost1 = self.helper(nums, cost, mid)
            cost2 = self.helper(nums, cost, mid + 1)
            if cost1 > cost2:
                left = mid + 1
                ans = cost2
            else:
                right = mid
                ans = cost1
        return ans
