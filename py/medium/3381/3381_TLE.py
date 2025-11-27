from itertools import accumulate
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums))
        res = -float("inf")
        for i in range(len(nums)):
            j = i + k - 1
            while j < len(nums):
                cur_sum = prefix_sums[j] - prefix_sums[i] + nums[i]
                res = max(res, cur_sum)
                j += k
        return res


s = Solution()
assert s.maxSubarraySum([1, 2], 1) == 3
assert s.maxSubarraySum([-1, -2, -3, -4, -5], 4) == -10
assert s.maxSubarraySum([-5, 1, 2, -3, 4], 2) == 4
