import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        negative_nums = [-x for x in nums]
        result = 0
        heapq.heapify(negative_nums)
        for _ in range(k):
            dr = -heapq.heappop(negative_nums)
            result += dr
            dr = -math.ceil(dr / 3)
            heapq.heappush(negative_nums, dr)
        return result


solution = Solution()
assert solution.maxKelements([10, 10, 10, 10, 10], 5) == 50
assert solution.maxKelements([1, 10, 3, 3, 3], 3) == 17
