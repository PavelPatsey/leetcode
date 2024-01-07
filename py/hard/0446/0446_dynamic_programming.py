from collections import Counter, defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [Counter() for _ in range(n)]
        total_count = 0

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]
        return total_count


solution = Solution()
assert solution.numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7
assert solution.numberOfArithmeticSlices([7, 7, 7, 7, 7]) == 16
