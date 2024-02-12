class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        res = maj = 0 

        for n in nums : 
            hash[n] = 1 + hash.get(n,0)
            if hash[n] > maj:
                res = n 
                maj = hash[n]

        return res
