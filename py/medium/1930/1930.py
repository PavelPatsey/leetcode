from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indexes = defaultdict(list)
        for i, c in enumerate(s):
            indexes[c].append(i)
        intervals = {k: (v[0], v[-1]) for k, v in indexes.items() if len(v) >= 2}
        ls = {char: len(set(s[v[0] + 1 : v[1]])) for char, v in intervals.items()}
        return sum(ls.values())


s = Solution()
assert s.countPalindromicSubsequence("aabca") == 3
assert s.countPalindromicSubsequence("adc") == 0
assert s.countPalindromicSubsequence("bbcbaba") == 4
