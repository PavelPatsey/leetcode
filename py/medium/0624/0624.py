from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value = max_value = arrays[0][0]
        for array in arrays:
            if array[0] < min_value:
                min_value = array[0]
            if array[-1] > max_value:
                max_value = array[-1]
        return abs(max_value - min_value)


solution = Solution()
assert solution.maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4
assert solution.maxDistance([[1], [1]]) == 0
assert solution.maxDistance([[1, 4], [0, 5]]) == 4
