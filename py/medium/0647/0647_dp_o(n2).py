class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        len_s = len(s)
        for i in range(len_s):
            left = right = i
            while left >= 0 and right < len_s and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left >= 0 and right < len_s and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count


solution = Solution()
assert solution.countSubstrings("abc") == 3
assert solution.countSubstrings("aaa") == 6
