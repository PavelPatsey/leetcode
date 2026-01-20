class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        return [f(n) for n in nums]


def f(n) -> int:
    x = 0
    while x <= n:
        if x | (x + 1) == n:
            return x
        x += 1
    return -1


solution = Solution()
assert solution.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3]
assert solution.minBitwiseArray([11, 13, 31]) == [9, 12, 15]
