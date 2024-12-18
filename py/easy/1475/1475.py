from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        res = []
        len_prices = len(prices)
        while i < len_prices:
            j = i + 1
            discount = None
            while j < len_prices and discount is None:
                if prices[j] <= prices[i]:
                    discount = prices[i] - prices[j]
                j += 1
            res.append(discount if discount is not None else prices[i])
            i += 1
        return res


solution = Solution()
assert solution.finalPrices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
assert solution.finalPrices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

lst_1 = [8, 7, 4, 2, 8, 1, 7, 7, 10, 1]
lst_2 = [1, 3, 2, 1, 7, 0, 0, 6, 9, 1]
assert solution.finalPrices(lst_1) == lst_2
