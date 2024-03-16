class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        n1=0
        n0=0
        maxLen=0
        mp={}
        mp[0]=-1
        for i in range(n):
            n1+=nums[i]
            n0=(i+1)-n1
            if (n1-n0) in mp:
                maxLen=max(maxLen, i-mp[n1-n0])
            else:
                mp[n1-n0]=i
        return maxLen
        
