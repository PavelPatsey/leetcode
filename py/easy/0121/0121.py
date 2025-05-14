class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        rev_prices = prices[::-1]
        max_x = rev_prices[0]
        diff = 0
        res = diff
        for x in rev_prices:
            if x > max_x:
                max_x = x
                diff = 0
            else:
                diff = max(diff, max_x - x)
                res = max(res, diff)
        return res


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
assert solution.maxProfit([1, 2]) == 1
