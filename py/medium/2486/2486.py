class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j


solution = Solution()
assert solution.appendCharacters("coaching", "coding") == 4
assert solution.appendCharacters("abcde", "a") == 0
assert solution.appendCharacters("z", "abcde") == 5
