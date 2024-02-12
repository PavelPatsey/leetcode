from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(Counter(nums).items(), key=lambda x: x[1])[0]


solution = Solution()
assert solution.majorityElement([3, 2, 3]) == 3
assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
