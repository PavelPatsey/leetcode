class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        cg = 0
        i = len(s) - 1
        while i >= 0:
            c = 0
            while i >= 0 and s[i] == "1":
                c += 1
                i -= 1
            while i >= 0 and s[i] == "0":
                i -= 1
            res += cg * c
            cg += 1
        return res


solution = Solution()
assert solution.maxOperations("1001101") == 4
assert solution.maxOperations("00111") == 0
