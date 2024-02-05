from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1


solution = Solution()
assert solution.firstUniqChar("leetcode") == 0
assert solution.firstUniqChar("loveleetcode") == 2
assert solution.firstUniqChar("aabb") == -1
