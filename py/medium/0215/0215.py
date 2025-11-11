class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        largest = []
        for n in nums:
            largest = add(n, k, largest)
        return min(largest)


def add(n: int, k: int, largest: list[int]) -> list[int]:
    largest.append(n)
    while len(largest) > k:
        largest.remove(min(largest))
    return largest


solution = Solution()
assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
