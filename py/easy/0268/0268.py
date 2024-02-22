from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = n * (n + 1) // 2
        return sum_n - sum(nums)


solutions = Solution()
assert solutions.missingNumber([3, 0, 1]) == 2
assert solutions.missingNumber([0, 1]) == 2
assert solutions.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
