from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        result = [0] * len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                result[i] = nums[k]
                i += 2
            else:
                result[j] = nums[k]
                j += 2
        return result


solution = Solution()
assert solution.rearrangeArray([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
