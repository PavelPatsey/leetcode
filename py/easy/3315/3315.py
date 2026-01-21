class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        def f(n) -> int:
            res = -1
            d = 1
            while d & n != 0:
                res = n - d
                d <<= 1
            return res

        return [f(n) for n in nums]


solution = Solution()
assert solution.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3]
assert solution.minBitwiseArray([11, 13, 31]) == [9, 12, 15]
