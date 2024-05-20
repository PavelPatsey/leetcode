from functools import reduce
from itertools import chain, combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def _get_powerset(iterable):
            s = list(iterable)
            return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

        def _get_xor(_nums: List[int]):
            if not _nums:
                return 0
            elif len(_nums) == 1:
                return _nums[0]
            else:
                return reduce(lambda i, j: int(i) ^ int(j), _nums, 0)

        return sum(map(_get_xor, _get_powerset(nums)))


solution = Solution()
assert solution.subsetXORSum([1, 3]) == 6
assert solution.subsetXORSum([5, 1, 6]) == 28
assert solution.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480
