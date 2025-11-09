class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ""
        for i in range(len(s)):
            l = r = i
            max_len, res = get_max_len_palindrome(l, r, s, max_len, res)
            l, r = i, i + 1
            max_len, res = get_max_len_palindrome(l, r, s, max_len, res)
        return res


def get_max_len_palindrome(l, r, s, max_len, palindrome):
    longest_palindrome = palindrome
    while 0 <= l and r < len(s) and s[l] == s[r]:
        new_len = r - l + 1
        if new_len > max_len:
            max_len = new_len
            longest_palindrome = s[l : r + 1]
        l = l - 1
        r = r + 1
    return max_len, longest_palindrome


solution = Solution()
assert solution.longestPalindrome("babad") in {"bab", "aba"}
assert solution.longestPalindrome("cbbd") == "bb"
