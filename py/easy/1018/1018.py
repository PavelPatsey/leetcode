from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        s = ""
        for n in nums:
            s += str(n)
            res.append(int(s, 2) % 5 == 0)
        return res


solution = Solution()
assert solution.prefixesDivBy5([0, 1, 1]) == [True, False, False]
assert solution.prefixesDivBy5([1, 1, 1]) == [False, False, False]
