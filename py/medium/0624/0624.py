from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_list = max_list = []
        for i, array in enumerate(arrays):
            min_list.append((i, array[0]))
            min_list = sorted(min_list, key=lambda x: x[1])
            if len(min_list) > 2:
                min_list.pop()

            max_list.append((i, array[-1]))
            max_list = sorted(max_list, key=lambda x: x[1])
            if len(max_list) > 2:
                max_list.pop(0)

        combinations = [
            (x[1], y[1]) for x in min_list for y in max_list if x[0] != y[0]
        ]
        return max(map(lambda x: abs(x[1] - x[0]), combinations))


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
