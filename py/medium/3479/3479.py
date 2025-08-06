from collections import deque


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        empties = [True] * len(baskets)
        for f in fruits:
            b = 0
            found = False
            while b < len(baskets) and not found:
                if f <= baskets[b] and empties[b]:
                    empties[b] = False
                    found = True
                b += 1
        return sum(empties)


solution = Solution()
assert solution.numOfUnplacedFruits([1, 1], [1, 1]) == 0
assert solution.numOfUnplacedFruits([4, 2, 5], [3, 5, 4]) == 1
assert solution.numOfUnplacedFruits([3, 6, 1], [6, 4, 7]) == 0
