class Solution:
    def solve(self, s1: str, s2: str, s3: str, ind1: int, ind2: int, dp: List[List[int]]) -> bool:
        if ind1 + ind2 == len(s3):
            return True
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2] == 1
        ans = False
        
        if ind1 < len(s1) and s1[ind1] == s3[ind1 + ind2]:
            ans |= self.solve(s1, s2, s3, ind1 + 1, ind2, dp)
        
        if ind2 < len(s2) and s2[ind2] == s3[ind1 + ind2]:
            ans |= self.solve(s1, s2, s3, ind1, ind2 + 1, dp)
        
        dp[ind1][ind2] = 1 if ans else 0
        return ans
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        return self.solve(s1, s2, s3, 0, 0, dp)
