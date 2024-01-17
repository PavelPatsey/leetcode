from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        values = Counter(arr).values()
        return len(set(values)) == len(values)


solution = Solution()
assert solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True
assert solution.uniqueOccurrences([1, 2]) is False
