class Solution:
    @staticmethod
    def is_palindromic(s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        max_palindrom = s[0]
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j + 1]
                condition = self.is_palindromic(substring) and len(substring) > len(
                    max_palindrom
                )
                if condition:
                    max_palindrom = substring
        return max_palindrom


solution = Solution()
assert solution.is_palindromic("a") == True
assert solution.is_palindromic("aba") == True
assert solution.is_palindromic("abad") == False
assert solution.longestPalindrome("babad") in {"bab", "aba"}
assert solution.longestPalindrome("cbbd") == "bb"
