from collections import defaultdict


class Solution:
    @staticmethod
    def is_valid_window(k: int, counter: defaultdict):
        replaces = sum(counter.values()) - max(counter.values())
        return replaces <= k

    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        l = r = 0
        counter = defaultdict(int)
        counter[s[r]] += 1
        while r < len(s):
            if self.is_valid_window(k, counter):
                result = max(r - l + 1, result)
                r += 1
                if r < len(s):
                    counter[s[r]] += 1
            else:
                counter[s[l]] -= 1
                l += 1
        return result


solution = Solution()
assert solution.characterReplacement("ABAB", 2) == 4
assert solution.characterReplacement("AABABBA", 1) == 4
assert solution.characterReplacement("A", 0) == 1
assert solution.characterReplacement("A", 1) == 1
assert solution.characterReplacement("ABBB", 2) == 4

assert solution.characterReplacement("BBBB", 0) == 4
assert solution.characterReplacement("ABAB", 0) == 1
