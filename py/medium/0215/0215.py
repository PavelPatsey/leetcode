import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        largest = []
        heapq.heapify(largest)
        for n in nums:
            largest = add(n, k, largest)
        return largest[0]


def add(n: int, k: int, largest: list[int]) -> list[int]:
    heapq.heappush(largest, n)
    while len(largest) > k:
        heapq.heappop(largest)
    return largest


solution = Solution()
assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
