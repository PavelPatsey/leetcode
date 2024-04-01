class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])


solution = Solution()
assert solution.lengthOfLastWord("Hello World") == 5
assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
assert solution.lengthOfLastWord("luffy is still joyboy") == 6
