class Solution:
    def minChanges(self, s: str) -> int:
        counter = 0
        for i in range(len(s) // 2):
            if s[2 * i] != s[2 * i + 1]:
                counter += 1
        return counter


solution = Solution()
assert solution.minChanges("1001") == 2
assert solution.minChanges("10") == 1
assert solution.minChanges("0000") == 0
