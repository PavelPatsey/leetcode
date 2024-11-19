from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter(nums[0:k])
        current_sum = sum(nums[0:k])
        result = current_sum if len(counter.keys()) == k else 0

        for i in range(1, len(nums) - k + 1):
            for_discard = nums[i - 1]
            counter[for_discard] -= 1
            if counter[for_discard] == 0:
                del counter[for_discard]
            current_sum -= for_discard
            for_add = nums[i + k - 1]
            counter[for_add] += 1
            current_sum += for_add
            result = max(result, current_sum if len(counter.keys()) == k else 0)
        return result


solution = Solution()
assert solution.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15
assert solution.maximumSubarraySum([4, 4, 4], 3) == 0
assert solution.maximumSubarraySum([1, 1, 1, 7, 8, 9], 3) == 24
assert solution.maximumSubarraySum([9, 9, 9, 1, 2, 3], 3) == 12
