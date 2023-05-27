class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        dp = defaultdict(int)
        for i in reversed(range(len(nums))):
            for is_alice in [True, False]:
                score = float(-inf) if is_alice else float(inf)
                for size in range(1, 4):
                    if is_alice:
                        score = max(score, sum(nums[i:i + size]) + dp[i + size, not is_alice])
                    else:
                        score = min(score, dp[i + size, not is_alice])
                dp[i, is_alice] = score
        a_score = dp[0, True]
        b_score = sum(nums) - a_score
        return "Alice" if a_score > b_score else "Bob" if a_score != b_score else "Tie"
