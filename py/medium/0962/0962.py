from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_list = [0] * len(nums)
        prev_max = 0
        for i, num in reversed(list(enumerate(nums))):
            max_list[i] = max(num, prev_max)
            prev_max = max_list[i]

        result = 0
        left = 0
        for right in range(len(nums)):
            while nums[left] > max_list[right]:
                left += 1
            result = max(result, right - left)
        return result


solution = Solution()
assert solution.maxWidthRamp([1, 2, 3, 4]) == 3
assert solution.maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4
assert solution.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7
