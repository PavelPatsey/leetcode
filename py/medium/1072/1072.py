from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = Counter()
        for row in matrix:
            pattern = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            counter[pattern] += 1
        return max(counter.values())


solution = Solution()
assert solution.maxEqualRowsAfterFlips([[0, 1], [1, 1]]) == 1
assert solution.maxEqualRowsAfterFlips([[0, 1], [1, 0]]) == 2
assert solution.maxEqualRowsAfterFlips([[0, 0, 0], [0, 0, 1], [1, 1, 0]]) == 2
