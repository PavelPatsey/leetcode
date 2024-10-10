from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] <= nums[j]:
                    result = max(result, j - i)
        return result


solution = Solution()
assert solution.maxWidthRamp([1, 2, 3, 4]) == 3
assert solution.maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4
assert solution.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
