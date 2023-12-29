from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()

assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert solution.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]
