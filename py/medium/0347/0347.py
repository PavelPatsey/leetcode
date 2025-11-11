import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        h = [(-freq, n) for n, freq in counter.items()]
        heapq.heapify(h)
        res = []
        for _ in range(k):
            _, n = heapq.heappop(h)
            res.append(n)
        return res


solution = Solution()
assert set(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
