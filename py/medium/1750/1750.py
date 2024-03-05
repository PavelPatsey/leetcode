class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while left < right and s[right] == char:
                right -= 1

        return right - left + 1


solution = Solution()
assert solution.minimumLength("ca") == 2
assert solution.minimumLength("aa") == 0
assert solution.minimumLength("cabaabac") == 0
