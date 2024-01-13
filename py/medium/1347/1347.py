from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return (Counter(s) - Counter(t)).total()


solution = Solution()
assert solution.minSteps("bab", "aba") == 1
assert solution.minSteps("leetcode", "practice") == 5
assert solution.minSteps("anagram", "mangaar") == 0
assert solution.minSteps("bab", "zab") == 1
