class Solution:
    @staticmethod
    def is_palindrome(string):
        return string == string[::-1]

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s[i : j + 1]):
                    count += 1
        return count


solution = Solution()
assert solution.countSubstrings("abc") == 3
assert solution.countSubstrings("aaa") == 6
