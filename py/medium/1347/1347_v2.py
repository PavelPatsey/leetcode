from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_c = Counter(s)
        counter_t = Counter(t)

        for key, value in counter_t.items():
            if key in counter_c:
                counter_c[key] -= counter_t[key]
            if counter_c[key] < 0:
                counter_c[key] = 0
        return sum(counter_c.values())


solution = Solution()
assert solution.minSteps("bab", "aba") == 1
assert solution.minSteps("leetcode", "practice") == 5
assert solution.minSteps("anagram", "mangaar") == 0
assert solution.minSteps("bab", "zab") == 1
assert solution.minSteps("z", "a") == 1
assert solution.minSteps("az", "aa") == 1
