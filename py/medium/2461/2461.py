from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums) - k + 1):
            if len(nums[i : i + k]) == len(set(nums[i : i + k])):
                result = max(result, sum(nums[i : i + k]))
        return result


solution = Solution()
assert solution.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15
assert solution.maximumSubarraySum([4, 4, 4], 3) == 0
