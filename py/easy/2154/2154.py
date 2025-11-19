class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums_set = set(nums)
        res = original
        while res in nums_set:
            res *= 2
        return res


s = Solution()
assert s.findFinalValue([5, 3, 6, 1, 12], 3) == 24
