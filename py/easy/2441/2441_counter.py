from collections import Counter
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        counter = Counter()
        result = -1
        for i in nums:
            if counter[-i] != 0:
                result = max(result, abs(i))
            counter[i] += 1
        return result


solution = Solution()
assert solution.findMaxK([-1, 2, -3, 3]) == 3
assert solution.findMaxK([-1, 10, 6, 7, -7, 1]) == 7
assert solution.findMaxK([-10, 8, 6, 7, -2, -3]) == -1
