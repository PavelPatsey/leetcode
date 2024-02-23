from collections import defaultdict, deque
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
        graph = defaultdict(list)
        for _from, _to, price in flights:
            graph[_from].append((_to, price))
        visited = [float("inf")] * n
        visited[src] = 0
        queue = deque([(src, 0)])
        steps = 0

        while steps <= k and queue:
            new_queue = deque()
            while queue:
                node, distance = queue.popleft()
                if node not in graph:
                    continue
                for neighbour, price in graph[node]:
                    if distance + price >= visited[neighbour]:
                        continue
                    visited[neighbour] = distance + price
                    new_queue.append((neighbour, visited[neighbour]))
            steps += 1
            queue = new_queue
        return visited[dst] if visited[dst] != float("inf") else -1


solution = Solution()
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
assert solution.findCheapestPrice(4, flights, 0, 3, 1) == 700

flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
assert solution.findCheapestPrice(3, flights, 0, 2, 0) == 500

flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
assert solution.findCheapestPrice(4, flights, 0, 3, 1) == 6
