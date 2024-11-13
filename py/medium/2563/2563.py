from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        return sum(
            True
            for i, nums_i in enumerate(nums)
            for j, nums_j in enumerate(nums[i + 1 :])
            if lower <= nums_i + nums_j <= upper
        )


solution = Solution()
assert solution.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6) == 6
assert solution.countFairPairs([1, 7, 9, 2, 5], 11, 11) == 1
