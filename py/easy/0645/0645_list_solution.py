from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeating_number = None
        n = len(nums)
        counter = [0] * n
        actual_sum = 0
        for num in nums:
            counter[num - 1] += 1
            if counter[num - 1] == 2:
                repeating_number = num
            actual_sum += num

        proper_sum = n * (n + 1) // 2
        missing_number = proper_sum - (actual_sum - repeating_number)
        return [repeating_number, missing_number]


solution = Solution()
assert solution.findErrorNums([1, 2, 2, 4]) == [2, 3]
assert solution.findErrorNums([1, 1]) == [1, 2]
assert solution.findErrorNums([2, 2]) == [2, 1]
assert solution.findErrorNums([3, 2, 2]) == [2, 1]
assert solution.findErrorNums([3, 2, 3, 4, 6, 5]) == [3, 1]
