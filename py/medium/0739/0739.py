from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        len_temperatures = len(temperatures)
        result = [0] * len_temperatures
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_i, stack_temp = stack.pop()
                result[stack_i] = i - stack_i
            stack.append((i, temp))
        return result


solution = Solution()
assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
