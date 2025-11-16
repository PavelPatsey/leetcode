class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        counter = 0
        res = 0
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == "1":
                counter += 1
                i += 1
            res += counter * (counter + 1) // 2
            while i < len(s) and s[i] == "0":
                i += 1
            counter = 0
        res += counter * (counter + 1) // 2
        res %= mod
        return res


solution = Solution()
assert solution.numSub("0110111") == 9
assert solution.numSub("101") == 2
assert solution.numSub("111111") == 21
