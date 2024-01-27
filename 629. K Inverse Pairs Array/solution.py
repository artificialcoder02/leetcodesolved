class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * 1001 for _ in range(1001)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                for x in range(0, min(j, i - 1) + 1):
                    if j - x >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % 1000000007

        return dp[n][k]
