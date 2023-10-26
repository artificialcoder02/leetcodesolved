class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        mod = int(1e9 + 7)
        arr.sort()
        ans = 0
        map = {}

        for x in arr:
            ways = 1
            max_val = int(x ** 0.5)

            j = 0
            left = arr[0]
            while left <= max_val:
                if x % left != 0:
                    j += 1
                    left = arr[j]
                    continue
                right = x // left
                if right in map:
                    ways = (ways + map[left] * map[right] * (1 if left == right else 2)) % mod
                j += 1
                left = arr[j]
            map[x] = ways
            ans = (ans + ways) % mod

        return ans
        
