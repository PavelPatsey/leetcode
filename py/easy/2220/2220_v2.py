class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        _max = max(start, goal)
        result = 0
        while _max:
            if (start & 1) != (goal & 1):
                result += 1
            _max = _max >> 1
            start = start >> 1
            goal = goal >> 1
        return result


solution = Solution()
assert solution.minBitFlips(10, 7) == 3
assert solution.minBitFlips(3, 4) == 3
