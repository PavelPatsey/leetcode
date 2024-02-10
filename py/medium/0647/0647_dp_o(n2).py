class Solution:
    @staticmethod
    def get_count(s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        len_s = len(s)
        for i in range(len_s):
            left = right = i
            count += self.get_count(s, left, right)

            left = i
            right = i + 1
            count += self.get_count(s, left, right)
        return count


solution = Solution()
assert solution.countSubstrings("abc") == 3
assert solution.countSubstrings("aaa") == 6
