from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        acc = 0
        result = -1
        for n in sorted_nums:
            if acc > n:
                result = acc + n
            acc += n
        return result


solution = Solution()
assert solution.largestPerimeter([1, 12, 1, 2, 5, 50, 3]) == 12
assert solution.largestPerimeter([5, 5, 5]) == 15
