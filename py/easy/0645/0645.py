from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_number = None
        repeating_number = None
        counter = Counter(nums)
        i = 1
        while missing_number is None or repeating_number is None:
            if counter[i] == 0:
                missing_number = i
            if counter[i] == 2:
                repeating_number = i
            i += 1
        return [repeating_number, missing_number]


solution = Solution()
assert solution.findErrorNums([1, 2, 2, 4]) == [2, 3]
assert solution.findErrorNums([1, 1]) == [1, 2]
assert solution.findErrorNums([2, 2]) == [2, 1]
assert solution.findErrorNums([3, 2, 2]) == [2, 1]
assert solution.findErrorNums([3, 2, 3, 4, 6, 5]) == [3, 1]
