import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = []
        for n, freq in counter.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for _f, n in heap]


solution = Solution()
assert set(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
