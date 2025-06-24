class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        js = [i for i, x in enumerate(nums) if x == key]
        return [i for i, x in enumerate(nums) if any(abs(i - j) <= k for j in js)]


solution = Solution()
assert solution.findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1) == [1, 2, 3, 4, 5, 6]
assert solution.findKDistantIndices([2, 2, 2, 2, 2], 2, 2) == [0, 1, 2, 3, 4]
