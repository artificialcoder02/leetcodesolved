class Solution(object):
    def minOperations(self, nums):
        nums.sort()

        res = 0
        s = 0
        while s < len(nums):
            e = s

            while e < len(nums) and nums[e] == nums[s]:
                e += 1
            count = e - s
            if count == 1:
                return -1
            res += count // 3

            if count % 3 != 0:
                res += 1
            s = e

        return res
        
