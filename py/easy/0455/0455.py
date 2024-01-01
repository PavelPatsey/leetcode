from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


solution = Solution()
assert solution.findContentChildren(g=[1, 2, 3], s=[1, 1]) == 1
assert solution.findContentChildren(g=[1, 2], s=[1, 2, 3]) == 2
assert solution.findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8]) == 2
