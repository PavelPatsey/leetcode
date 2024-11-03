class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


solution = Solution()
assert solution.rotateString("abcde", "cdeab") is True
assert solution.rotateString("abcde", "abced") is False
