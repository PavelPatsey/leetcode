class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        res = 0
        while right <= len(s):
            current = s[left:right]
            if len(current) == len(set(current)):
                res = max(right - left, res)
                right += 1
            else:
                left += 1
        return res


solution = Solution()
assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("abc") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3
