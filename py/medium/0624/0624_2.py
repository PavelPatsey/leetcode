from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        cur_min, cur_max = float("inf"), -float("inf")
        for array in arrays:
            result = max(result, cur_max - array[0], array[-1] - cur_min)
            cur_min = min(cur_min, array[0])
            cur_max = max(cur_max, array[-1])
        return result


solution = Solution()
assert solution.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4
assert solution.maxDistance([[1], [1]]) == 0
assert solution.maxDistance([[1, 4], [0, 5]]) == 4
assert solution.maxDistance([[-1, 5], [1, 4, 6], [4, 5, 6]]) == 7
assert (
    solution.maxDistance(
        [[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]
    )
    == 14
)
assert solution.maxDistance([[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]]) == 6
