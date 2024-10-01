from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        reminders = list(map(lambda x: x % k, arr))
        frequencies = Counter(reminders)
        if frequencies[0] % 2 != 0:
            return False
        for i in range(1, k // 2 + 1):
            if frequencies[i] != frequencies[k - i]:
                return False
        return True


solution = Solution()
assert solution.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5) is True
assert solution.canArrange([1, 2, 3, 4, 5, 6], 7) is True
assert solution.canArrange([1, 2, 3, 4, 5, 6], 10) is False
assert solution.canArrange([-1, 1, -2, 2, -3, 3, -4, 4], 3) is True
