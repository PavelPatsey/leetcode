from collections import Counter
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counter = Counter()
        for n in candidates:
            i = 0
            while n > 0:
                counter[i] += 1 & n
                i += 1
                n = n >> 1
        return max(counter.values())


solution = Solution()
assert solution.largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4
assert solution.largestCombination([8, 8]) == 2
