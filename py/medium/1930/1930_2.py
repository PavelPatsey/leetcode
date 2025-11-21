class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        chars = set(s)
        for char in chars:
            first = s.find(char)
            last = s.rfind(char)
            if first != last:
                res += len(set(s[first + 1 : last]))
        return res


solution = Solution()
assert solution.countPalindromicSubsequence("aabca") == 3
assert solution.countPalindromicSubsequence("adc") == 0
assert solution.countPalindromicSubsequence("bbcbaba") == 4
