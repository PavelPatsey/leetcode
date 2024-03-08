from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = Counter(nums)
        max_frequency = max(frequencies.values())
        filtered = filter(lambda x: x[1] == max_frequency, frequencies.items())
        mapped = map(lambda x: x[1], filtered)
        return sum(mapped)


solution = Solution()
assert solution.maxFrequencyElements([1, 2, 2, 3, 1, 4]) == 4
assert solution.maxFrequencyElements([1, 2, 3, 4, 5]) == 5
