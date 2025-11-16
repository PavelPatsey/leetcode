class Solution:
    def numSub(self, s: str) -> int:
        res = sum(len(x) * (len(x) + 1) // 2 for x in s.split("0"))
        res %= 10**9 + 7
        return res


solution = Solution()
assert solution.numSub("0110111") == 9
assert solution.numSub("101") == 2
assert solution.numSub("111111") == 21
