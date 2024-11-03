class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        i = 0
        while i < len(s):
            if s[i + 1 :] + s[: i + 1] == goal:
                return True
            i += 1
        return False


solution = Solution()
assert solution.rotateString("abcde", "cdeab") is True
assert solution.rotateString("abcde", "abced") is False
