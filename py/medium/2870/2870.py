from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if 1 in counter.values():
            return -1
        answer = 0
        for value in counter.values():
            answer += value // 3 + (value % 3 != 0)
        return answer


solution = Solution()

# assert solution.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
# assert solution.minOperations([2, 1, 2, 2, 3, 3]) == -1
assert solution.minOperations([16, 16, 16, 19, 16, 3, 16, 8, 16, 16, 16, 19, 3, 16, 16]) == -1
