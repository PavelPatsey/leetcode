class Solution:
    def numSub(self, s: str) -> int:
        counter = 0
        res = 0
        for char in s:
            if char == "0":
                res += counter * (counter + 1) // 2
                counter = 0
            elif char == "1":
                counter += 1
        res += counter * (counter + 1) // 2
        res = res % (10**9 + 7)
        return res


solution = Solution()
assert solution.numSub("0110111") == 9
assert solution.numSub("101") == 2
assert solution.numSub("111111") == 21
