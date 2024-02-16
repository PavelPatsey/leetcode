from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        values = list(Counter(arr).values())
        sorted_values = sorted(values, reverse=True)
        result = len(sorted_values)
        while sorted_values and k > 0:
            value = sorted_values.pop()
            if k >= value:
                result -= 1
            k -= value
        return result


solution = Solution()
assert solution.findLeastNumOfUniqueInts([5, 5, 4], 1) == 1
assert solution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3) == 2
assert solution.findLeastNumOfUniqueInts([2, 1, 1, 3, 3, 3], 3) == 1
