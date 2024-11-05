class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))


solution = Solution()
assert solution.minChanges("1001") == 2
assert solution.minChanges("10") == 1
assert solution.minChanges("0000") == 0
