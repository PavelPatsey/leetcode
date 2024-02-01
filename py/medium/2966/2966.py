from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = 3
        chunked_nums = []
        for i in range(0, len(sorted_nums), n):
            chunk = sorted_nums[i : i + n]
            if chunk[2] - chunk[0] <= k:
                chunked_nums.append(chunk)
            else:
                break
        else:
            return chunked_nums
        return []


solution = Solution()
assert solution.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2) == [
    [1, 1, 3],
    [3, 4, 5],
    [7, 8, 9],
]
assert solution.divideArray([1, 3, 3, 2, 7, 3], 3) == []
assert (
    solution.divideArray(
        [15, 13, 12, 13, 12, 14, 12, 2, 3, 13, 12, 14, 14, 13, 5, 12, 12, 2, 13, 2, 2],
        2,
    )
    == []
)
