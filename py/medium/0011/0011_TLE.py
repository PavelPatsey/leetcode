class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                res = max(res, area(i, j, height))
        return res


def area(i, j, height) -> int:
    return (j - i) * min(height[i], height[j])


solution = Solution()
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solution.maxArea([1, 1]) == 1
