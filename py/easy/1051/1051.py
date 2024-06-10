from functools import reduce
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        filtered = filter(lambda x: x[0] != x[1], zip(heights, sorted_heights))
        result = reduce(lambda acc, x: acc + 1, filtered, 0)
        return result


solution = Solution()
assert solution.heightChecker([1, 1, 4, 2, 1, 3]) == 3
assert solution.heightChecker([5, 1, 2, 3, 4]) == 5
assert solution.heightChecker([1, 2, 3, 4, 5]) == 0
