class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        res = 0
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if nums[i] == 0:
                if left == right:
                    res += 2
                elif abs(left - right) == 1:
                    res += 1
                else:
                    pass
            left += nums[i]
        return res


solution = Solution()
assert solution.countValidSelections([1, 0, 2, 0, 3]) == 2
assert solution.countValidSelections([2, 3, 4, 0, 4, 1, 0]) == 0
assert solution.countValidSelections([0, 2, 3, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 10]) == 14


assert solution.countValidSelections([1, 0, 0]) == 2
