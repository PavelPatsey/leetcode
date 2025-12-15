class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        res = 0
        c = 1
        prev = float("inf")
        for p in prices:
            if p == prev - 1:
                c += 1
            else:
                res += (c * (c + 1)) // 2
                c = 1
            prev = p
        res += (c * (c + 1)) // 2
        return res - 1


solution = Solution()
assert solution.getDescentPeriods([3, 2, 1, 4]) == 7
assert solution.getDescentPeriods([8, 6, 7, 7]) == 4
assert solution.getDescentPeriods([8, 6, 3]) == 3
