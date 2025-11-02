class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = new_sum = sum(nums[0:k])
        i = 1
        while i + k - 1 < len(nums):
            left = i
            right = i + k - 1
            new_sum = new_sum + nums[right] - nums[left - 1]
            max_sum = max(max_sum, new_sum)
            i += 1
        return max_sum / k


solution = Solution()
assert solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
assert solution.findMaxAverage([5], 1) == 5
