from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        matrix = [[] for _ in range(max(counter.values()))]
        for key, value in counter.items():
            for i in range(value):
                matrix[i].append(key)
        return matrix


solution = Solution()
found_matrix = solution.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1])
test_matrix = [[1, 3, 4, 2], [1, 3], [1]]
assert [set(x) for x in found_matrix] == [set(x) for x in test_matrix]

found_matrix = solution.findMatrix(nums=[1, 2, 3, 4])
test_matrix = [[4, 3, 2, 1]]
assert [set(x) for x in found_matrix] == [set(x) for x in test_matrix]
