
class Solution(object):
    def hammingWeight(self, n):
        set_bit_count = 0
        while n != 0:
            n &= (n - 1)
            set_bit_count += 1
        return set_bit_count
        
