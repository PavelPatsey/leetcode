from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        l, r = 0, len(sorted_nums) - 1
        result = -1
        while l < r and result == -1:
            diff = sorted_nums[l] + sorted_nums[r]
            if diff > 0:
                r -= 1
            elif diff < 0:
                l += 1
            elif diff == 0:
                result = sorted_nums[r]
            else:
                raise Exception("error")
        return result


solution = Solution()
assert solution.findMaxK([-1, 2, -3, 3]) == 3
assert solution.findMaxK([-1, 10, 6, 7, -7, 1]) == 7
assert solution.findMaxK([-10, 8, 6, 7, -2, -3]) == -1
