class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        exclusive_or = start ^ goal
        while exclusive_or:
            if exclusive_or & 1:
                result += 1
            exclusive_or = exclusive_or >> 1
        return result


solution = Solution()
assert solution.minBitFlips(10, 7) == 3
assert solution.minBitFlips(3, 4) == 3
