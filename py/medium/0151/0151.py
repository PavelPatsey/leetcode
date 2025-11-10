class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.strip().split()
        return " ".join(reversed(splitted))


solution = Solution()
assert solution.reverseWords("the sky is blue") == "blue is sky the"
