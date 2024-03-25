from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for n in nums:
            number = abs(n)
            if nums[number - 1] < 0:
                result.append(number)
            else:
                nums[number - 1] *= -1
        return result


solution = Solution()
assert solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
assert solution.findDuplicates([1, 1, 2]) == [1]
assert solution.findDuplicates([1]) == []
