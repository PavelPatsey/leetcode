class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = -float("inf")
        i = 0
        while i + k - 1 < len(nums):
            max_sum = max(max_sum, sum(nums[i : i + k]))
            i += 1
        return max_sum / k


solution = Solution()
assert solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
assert solution.findMaxAverage([5], 1) == 5
