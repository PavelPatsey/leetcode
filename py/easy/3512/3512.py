from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k


s = Solution()
assert s.minOperations([3, 9, 7], 5) == 4
assert s.minOperations([4, 1, 3], 4) == 0
assert s.minOperations([3, 2], 6) == 5
