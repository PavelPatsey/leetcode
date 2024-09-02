from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        current_k = k % sum_chalk
        for i, value in enumerate(chalk):
            if current_k < value:
                break
            current_k -= value
        return i


solution = Solution()
assert solution.chalkReplacer([3, 4], 7) == 0
assert solution.chalkReplacer([3, 5], 7) == 1
assert solution.chalkReplacer([5, 1, 5], 22) == 0
assert solution.chalkReplacer([3, 4, 1, 2], 25) == 1
