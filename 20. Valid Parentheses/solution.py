class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen={")":"(","}":"{","]":"["}

        for c in s :
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False

        
