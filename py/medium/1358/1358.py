class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            substring = s[i:]
            char_set = set()
            for x, char in enumerate(substring):
                char_set.add(char)
                if len(char_set) == 3:
                    d_res = len(substring) - x
                    res += d_res
                    break
        return res


solution = Solution()
assert solution.numberOfSubstrings("abcabc") == 10
assert solution.numberOfSubstrings("aaacb") == 3
