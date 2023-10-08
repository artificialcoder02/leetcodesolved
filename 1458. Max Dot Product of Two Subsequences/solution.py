class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        current = [float('-inf')] * (n + 1)
        previous = [float('-inf')] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_product = nums1[i-1] * nums2[j-1]
                
                current[j] = max(curr_product, previous[j], current[j-1], curr_product + max(0, previous[j-1]))
            
            current, previous = previous, current
        
        return previous[n]
