import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        enumerated = list(enumerate(nums))
        result = 0
        for _ in range(k):
            max_item = max(enumerated, key=lambda x: x[1])
            max_ind = max_item[0]
            item = math.ceil(enumerated[max_ind][1] / 3)
            result += enumerated[max_ind][1]
            enumerated[max_ind] = (max_ind, item)
        return result


solution = Solution()
assert solution.maxKelements([10, 10, 10, 10, 10], 5) == 50
assert solution.maxKelements([1, 10, 3, 3, 3], 3) == 17
