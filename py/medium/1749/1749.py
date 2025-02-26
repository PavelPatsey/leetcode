from itertools import accumulate
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)


solution = Solution()
assert solution.maxAbsoluteSum([1, -3, 2, 3, -4]) == 5
assert solution.maxAbsoluteSum([2, -5, 1, -4, 3, -2]) == 8
assert (
    solution.maxAbsoluteSum(
        [-3, -5, -3, -2, -6, 3, 10, -10, -8, -3, 0, 10, 3, -5, 8, 7, -9, -9, 5, -8]
    )
    == 27
)
