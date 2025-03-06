class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        reference_sum = n * n * (n * n + 1) // 2
        nums_set = set()
        real_sum = 0
        for row in grid:
            for x in row:
                nums_set.add(x)
                real_sum += x
        missing_num = reference_sum - sum(nums_set)
        ds = real_sum - reference_sum
        repeating_num = missing_num + ds
        return [repeating_num, missing_num]


solution = Solution()
assert solution.findMissingAndRepeatedValues([[1, 3], [2, 2]]) == [2, 4]
assert solution.findMissingAndRepeatedValues([[9, 1, 7], [8, 9, 2], [3, 4, 6]]) == [
    9,
    5,
]
