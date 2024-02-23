from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        def _find_cheapest_price(node, acc, step):
            if node == dst:
                return acc
            if step > k or node not in graph:
                return float("inf")
            return min(
                [
                    _find_cheapest_price(to_city, acc + cost, step + 1)
                    for to_city, cost in graph[node]
                ]
            )

        graph = defaultdict(list)
        for _from, _to, price in flights:
            graph[_from].append((_to, price))
        result = _find_cheapest_price(src, 0, 0)
        return -1 if result == float("inf") else result


solution = Solution()
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
assert solution.findCheapestPrice(4, flights, 0, 3, 1) == 700

flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
assert solution.findCheapestPrice(3, flights, 0, 2, 0) == 500
