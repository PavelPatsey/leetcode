class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        if len(diff) == 0:
            return True
        elif len(diff) == 2:
            i, j = diff
            return s1[i] == s2[j] and s1[j] == s2[i]
        else:
            return False


solution = Solution()
assert solution.areAlmostEqual("bank", "kanb") is True
assert solution.areAlmostEqual("attack", "defend") is False
assert solution.areAlmostEqual("kelb", "kelb") is True
assert solution.areAlmostEqual("qgqeg", "gqgeq") is False
