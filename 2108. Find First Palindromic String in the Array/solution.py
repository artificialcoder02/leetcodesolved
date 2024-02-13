class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((s for s in words if all(s[i]==s[-(i+1)] for i in range(len(s)//2))), "")
