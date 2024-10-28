from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        counter = 0
        visited = set()
        for num in sorted_nums:
            current_set = set([num])
            squared = num * num
            while squared in sorted_nums and squared not in visited:
                visited.add(squared)
                current_set.add(squared)
                squared = squared * squared
            if len(current_set) > 1:
                counter += len(current_set)
        return counter if counter else -1


solution = Solution()
assert solution.longestSquareStreak([4, 3, 6, 16, 8, 2]) == 3
assert solution.longestSquareStreak([2, 3, 5, 6, 7]) == -1
assert solution.longestSquareStreak([2, 4, 16, 3, 9]) == 5
assert solution.longestSquareStreak([2, 4, 16, 3, 3, 3, 9]) == 5
