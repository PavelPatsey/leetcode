class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if n - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        return dp[n]


solution = Solution()
assert solution.numSquares(5) == 2
assert solution.numSquares(12) == 3
assert solution.numSquares(13) == 2
