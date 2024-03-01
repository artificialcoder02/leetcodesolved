class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count("1")
        zeroes_count = len(s) - ones_count

        return "1" * (ones_count - 1 ) + "0" * zeroes_count + "1"
