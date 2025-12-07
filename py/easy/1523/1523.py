class Solution:
    def countOdds(self, low: int, high: int) -> int:
        dx = high - low + 1
        if dx % 2 == 0:
            return dx // 2
        return dx // 2 + low % 2


s = Solution()
assert s.countOdds(3, 7) == 3
assert s.countOdds(8, 10) == 1
