class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        for i in range(len(prices)):
            first = prices[i]
            for x in prices[i + 1 :]:
                if x > first:
                    res = max(res, x - first)
        return res


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
