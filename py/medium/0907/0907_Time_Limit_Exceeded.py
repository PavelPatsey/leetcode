from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        len_arr = len(arr)
        mins = (
            min(arr[start:end])
            for start in range(len_arr)
            for end in range(start + 1, len_arr + 1)
        )
        return sum(mins) % (10**9 + 7)


solution = Solution()
assert solution.sumSubarrayMins([3, 1, 2, 4]) == 17
assert solution.sumSubarrayMins([11, 81, 94, 43, 3]) == 444
