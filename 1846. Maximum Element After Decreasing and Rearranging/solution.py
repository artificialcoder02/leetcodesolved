class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans=1
        for x in arr[1:]:
            ans=min(x, ans+1)
        return ans
        
