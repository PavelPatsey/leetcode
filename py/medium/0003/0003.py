class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        res = 0
        char_set = set()
        while right < len(s):
            new_char = s[right]
            if new_char in char_set:
                while new_char in char_set:
                    char_set.remove(s[left])
                    left += 1
            char_set.add(new_char)
            right += 1
            res = max(res, right - left)
        return res


solution = Solution()
assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("abc") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3
assert solution.lengthOfLongestSubstring("aab") == 2
