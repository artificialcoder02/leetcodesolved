class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        l=0
        for i in pushed:
            stack+=[i]
            while len(stack)>0 and stack[-1]==popped[l]:
                stack.pop()
                l+=1
        return len(stack)==0
