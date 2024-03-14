from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            j = i
            current_sum = 0
            while j < len_nums and current_sum <= goal:
                current_sum += nums[j]
                if current_sum == goal:
                    result += 1
                j += 1

            i += 1
        return result


solution = Solution()
assert solution.numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4
assert solution.numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15
