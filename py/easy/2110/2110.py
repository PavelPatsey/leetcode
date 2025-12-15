class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        c = 1
        res = 1
        for prev, cur in zip(prices, prices[1:]):
            if cur == prev - 1:
                c += 1
            else:
                c = 1
            res += c
        return res


solution = Solution()
assert solution.getDescentPeriods([3, 2, 1, 4]) == 7
assert solution.getDescentPeriods([8, 6, 7, 7]) == 4
