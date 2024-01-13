class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0

        for char in set(t):
            diff = t.count(char) - s.count(char)
            res += diff if diff > 0 else 0
        
        return res
