from functools import lru_cache


@lru_cache
def is_palindromic(s: str) -> bool:
    if s == "":
        return True
    if len(s) == 1:
        return True
    if s[0] == s[-1]:
        substring = s[1 : len(s) - 1]
        return is_palindromic(substring)
    return False


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        while length > 0:
            start = 0
            while start + length <= len(s):
                if is_palindromic(s[start : start + length]):
                    return s[start : start + length]
                start += 1
            length -= 1
        return s[0]


solution = Solution()
assert is_palindromic("") == True
assert is_palindromic("a") == True
assert is_palindromic("aba") == True
assert is_palindromic("abad") == False

assert solution.longestPalindrome("babad") in {"bab", "aba"}
assert solution.longestPalindrome("cbbd") == "bb"
