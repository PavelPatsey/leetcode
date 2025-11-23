from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        smallest_one = float("inf")
        smallest_two = float("inf")
        for n in nums:
            total += n
            if n % 3 == 1:
                smallest_two = min(smallest_two, n + smallest_one)
                smallest_one = min(smallest_one, n)
            elif n % 3 == 2:
                smallest_one = min(smallest_one, n + smallest_two)
                smallest_two = min(smallest_two, n)
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            return total - smallest_one
        else:
            return total - smallest_two


s = Solution()
assert s.maxSumDivThree([3, 6, 5, 1, 8]) == 18
assert s.maxSumDivThree([4]) == 0
assert s.maxSumDivThree([1, 2, 3, 4, 4]) == 12
