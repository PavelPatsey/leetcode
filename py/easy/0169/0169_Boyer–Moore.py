from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = None, 0
        for num in nums:
            if count == 0:
                result = num
            count += 1 if result == num else -1
        return result


solution = Solution()

assert solution.majorityElement([3, 2, 3]) == 3
assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
