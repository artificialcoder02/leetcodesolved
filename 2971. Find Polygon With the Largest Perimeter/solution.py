
from itertools import accumulate
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        prefix = list(accumulate(nums))
        for i in range(n-1,-1,-1):
            if i<2:
                return -1 
            x = nums[i]
            if prefix[i-1]>x:
                return x+ prefix[i-1]
        return -1 
        
