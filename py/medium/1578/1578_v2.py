from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        i = 0
        j = 0
        len_list = len(neededTime)

        while i < len_list and j < len_list:
            delta_time = 0
            max_time = 0

            while j < len_list and colors[i] == colors[j]:
                delta_time += neededTime[j]
                max_time = max(max_time, neededTime[j])
                j += 1

            delta_time -= max_time
            total_time += delta_time
            i = j

        return total_time


solution = Solution()

colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
assert solution.minCost(colors, neededTime) == 3

colors = "abc"
neededTime = [1, 2, 3]
assert solution.minCost(colors, neededTime) == 0

colors = "aabaa"
neededTime = [1, 2, 3, 4, 1]
assert solution.minCost(colors, neededTime) == 2

colors = "abbbbba"
neededTime = [1, 2, 3, 4, 5, 6, 7]
assert solution.minCost(colors, neededTime) == 14

colors = "aaabbbabbbb"
neededTime = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
assert solution.minCost(colors, neededTime) == 26
