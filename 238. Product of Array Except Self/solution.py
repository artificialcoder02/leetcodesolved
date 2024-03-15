class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [0] * n
        product = 1
        zeros = 0
        
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            product *= num

        if zeros == 1:
            for i in range(n):
                ans[i] = product if nums[i] == 0 else 0
        elif zeros == 0:
            for i in range(n):
                ans[i] = product // nums[i]

        return ans
