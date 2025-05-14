class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_x = prices[0]
        res = 0
        for x in prices:
            if x < min_x:
                min_x = x
            else:
                res = max(res, x - min_x)
        return res


solution = Solution()
assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
assert solution.maxProfit([1, 2]) == 1
