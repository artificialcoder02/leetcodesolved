class Solution:
    def longestSubarray(self, nums):
        num_of_zeros_allowed = 1
        left_ptr = 0
        right_ptr = 0

        for right_ptr in range(len(nums)):
            num_of_zeros_allowed -= nums[right_ptr] == 0
            if num_of_zeros_allowed < 0:
                num_of_zeros_allowed += nums[left_ptr] == 0
                left_ptr += 1

        return right_ptr - left_ptr
