from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = -1
        for i in nums_set:
            if -i in nums_set:
                result = max(result, abs(i))
        return result


solution = Solution()
assert solution.findMaxK([-1, 2, -3, 3]) == 3
assert solution.findMaxK([-1, 10, 6, 7, -7, 1]) == 7
assert solution.findMaxK([-10, 8, 6, 7, -2, -3]) == -1
