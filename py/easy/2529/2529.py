class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos = 0
        neg = 0
        for n in nums:
            if n > 0:
                pos += 1
            elif n < 0:
                neg += 1
            else:
                pass
        return max(neg, pos)


solution = Solution()
assert solution.maximumCount([-2, -1, -1, 1, 2, 3]) == 3
assert solution.maximumCount([-3, -2, -1, 0, 0, 1, 2]) == 3
assert solution.maximumCount([5, 20, 66, 1314]) == 4
