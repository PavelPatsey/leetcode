class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split()
        return " ".join(reversed(splitted))


solution = Solution()
assert solution.reverseWords("the sky is blue") == "blue is sky the"
assert solution.reverseWords("  hello world  ") == "world hello"
