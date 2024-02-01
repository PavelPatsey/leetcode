from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer_list = []
        len_temperatures = len(temperatures)
        for i in range(len_temperatures):
            j = i + 1
            while j < len_temperatures and temperatures[j] <= temperatures[i]:
                j = j + 1
            answer_list.append(j - i if j < len_temperatures else 0)
        return answer_list


solution = Solution()
assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
