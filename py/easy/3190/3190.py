from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            if x % 3 != 0:
                res += 1
        return res


solution = Solution()
assert solution.minimumOperations([1, 2, 3, 4]) == 3
assert solution.minimumOperations([3, 6, 9]) == 0
