from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        sorted_nums = sorted(num_set)
        longest_streak = -1
        for num in sorted_nums:
            streak = 0
            current = num
            while current in num_set:
                streak += 1
                current = current * current
            if streak > 1:
                longest_streak = max(longest_streak, streak)
        return longest_streak


solution = Solution()
assert solution.longestSquareStreak([4, 3, 6, 16, 8, 2]) == 3
assert solution.longestSquareStreak([2, 3, 5, 6, 7]) == -1
assert solution.longestSquareStreak([2, 4, 16, 3, 9]) == 3
assert solution.longestSquareStreak([2, 4, 16, 3, 3, 3, 9]) == 3
