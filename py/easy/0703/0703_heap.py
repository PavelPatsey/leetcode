from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


obj = KthLargest(3, [4, 5, 8, 2])
assert obj.add(3) == 4
assert obj.add(5) == 5
assert obj.add(10) == 5
assert obj.add(9) == 8
assert obj.add(4) == 8
