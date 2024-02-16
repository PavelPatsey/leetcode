import heapq
from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        values = list(Counter(arr).values())
        heapq.heapify(values)
        result = len(values)
        while values and k > 0:
            value = heapq.heappop(values)
            if k >= value:
                result -= 1
            k -= value
        return result


solution = Solution()
assert solution.findLeastNumOfUniqueInts([5, 5, 4], 1) == 1
assert solution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3) == 2
assert solution.findLeastNumOfUniqueInts([2, 1, 1, 3, 3, 3], 3) == 1
