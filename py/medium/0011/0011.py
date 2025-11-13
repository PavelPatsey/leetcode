class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            hl, hr = height[l], height[r]
            area = (r - l) * min(hl, hr)
            res = max(res, area)
            if hl < hr:
                l += 1
            else:
                r -= 1
        return res


solution = Solution()
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solution.maxArea([1, 1]) == 1
assert solution.maxArea([1, 2, 4, 3]) == 4
