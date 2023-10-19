class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process_string(string):
            k = 0
            for i in range(len(string)):
                if string[i] != '#':
                    string[k] = string[i]
                    k += 1
                else:
                    k = max(k-1, 0)
            return k
        
        # Convert strings to lists for in-place modifications
        s, t = list(s), list(t)
        
        k = process_string(s)
        p = process_string(t)
        
        # If effective lengths are different, return False
        if k != p:
            return False
        
        # Compare the effective characters
        for i in range(k):
            if s[i] != t[i]:
                return False
        
        return True
