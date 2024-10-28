from typing import List


class Solution:
    MAX_NUMBER = 100_000

    def longestSquareStreak(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        longest_square_streak = -1
        visited = set()
        for num in sorted_nums:
            current_set = set([num])
            squared = num * num
            while (
                squared <= self.MAX_NUMBER
                and squared not in visited
                and self.find_in_sorted_list(squared, sorted_nums) != -1
            ):
                visited.add(squared)
                current_set.add(squared)
                squared = squared * squared

            if len(current_set) > 1:
                longest_square_streak = max(longest_square_streak, len(current_set))
        return longest_square_streak

    @staticmethod
    def find_in_sorted_list(number: int, sorted_list: List[int]) -> int:
        left, right = 0, len(sorted_list) - 1
        mid = len(sorted_list) // 2

        while sorted_list[mid] != number and left <= right:
            if number > sorted_list[mid]:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2

        return -1 if left > right else mid


solution = Solution()
assert solution.find_in_sorted_list(1, [1, 2, 3]) == 0
assert solution.find_in_sorted_list(3, [1, 2, 3]) == 2
assert solution.find_in_sorted_list(10, [1, 2, 3]) == -1


assert solution.longestSquareStreak([4, 3, 6, 16, 8, 2]) == 3
assert solution.longestSquareStreak([2, 3, 5, 6, 7]) == -1
assert solution.longestSquareStreak([2, 4, 16, 3, 9]) == 3
assert solution.longestSquareStreak([2, 4, 16, 3, 3, 3, 9]) == 3
