from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_k = (1 << maximumBit) - 1
        prev = nums[0]
        result = [(prev | max_k) ^ prev]
        for num in nums[1:]:
            prev = prev ^ num
            result.append((prev | max_k) ^ prev)
        return result[::-1]


solution = Solution()
assert solution.getMaximumXor([0, 1, 1, 3], 2) == [0, 3, 2, 3]
assert solution.getMaximumXor([2, 3, 4, 7], 3) == [5, 2, 6, 5]
assert solution.getMaximumXor([0, 1, 2, 2, 5, 7], 3) == [4, 3, 6, 4, 6, 7]
