from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        bin_n = 0
        for bit in nums:
            bin_n = (bin_n << 1) | bit
            bin_n = bin_n % 5
            res.append(bin_n == 0)
        return res


solution = Solution()
assert solution.prefixesDivBy5([0, 1, 1]) == [True, False, False]
assert solution.prefixesDivBy5([1, 1, 1]) == [False, False, False]
