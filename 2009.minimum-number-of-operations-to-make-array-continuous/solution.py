class Solution(object):
    def minOperations(self, nums):
        # Sort the input list in ascending order.
        nums.sort()
        
        # Initialize variables to keep track of unique elements and minimum operations.
        unique_len = 1
        ans = len(nums)
        
        # Traverse the sorted list to remove duplicates and count unique elements.
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_len] = nums[i]
                unique_len += 1
        
        # Initialize pointers for calculating operations within subarrays.
        i, j = 0, 0
        
        # Iterate over unique elements to find minimum operations.
        for i in range(unique_len):
            while j < unique_len and nums[j] - nums[i] <= len(nums) - 1:
                j += 1
            ans = min(ans, len(nums) - (j - i))
        
        return ans
