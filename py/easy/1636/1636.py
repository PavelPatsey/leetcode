from collections import Counter
from functools import cmp_to_key
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        def _compare(key_1, key_2):
            value_1, value_2 = counter[key_1], counter[key_2]
            if value_1 == value_2:
                return key_2 - key_1
            else:
                return value_1 - value_2

        counter = Counter(nums)
        return sorted(nums, key=cmp_to_key(_compare))


solution = Solution()
assert solution.frequencySort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
assert solution.frequencySort([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]
assert solution.frequencySort([1, 5, 0, 5]) == [1, 0, 5, 5]
