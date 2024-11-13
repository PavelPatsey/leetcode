from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sorted_nums = sorted(set(nums))
        n = len(nums)
        counter = 0
        for i in range(n):
            for j in range(i, n):
                if 0 <= i < j < n and lower <= nums[i] + nums[j] <= upper:
                    counter += 1
        return counter


solution = Solution()
assert solution.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6) == 6
assert solution.countFairPairs([1, 7, 9, 2, 5], 11, 11) == 1
