class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        i = 0
        a, b=0, 0
        for i in range(len(s)//2):
            if s[i] in v:
                a+=1
            if s[-i-1] in v:
                b+=1
        return a==b
        
