from collections import deque
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        subarray = deque(nums[0:k])
        result = sum(subarray) if len(subarray) == len(set(subarray)) else 0
        current_sum = sum(subarray)

        for i in range(1, len(nums) - k + 1):
            current_sum -= subarray.popleft()
            subarray.append(nums[i + k - 1])
            current_sum += nums[i + k - 1]
            result = max(
                result,
                current_sum if len(subarray) == len(set(subarray)) else 0,
            )
        return result


solution = Solution()
assert solution.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15
assert solution.maximumSubarraySum([4, 4, 4], 3) == 0
assert solution.maximumSubarraySum([1, 1, 1, 7, 8, 9], 3) == 24
