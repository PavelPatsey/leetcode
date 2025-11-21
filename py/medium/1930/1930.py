from collections import defaultdict
from typing import List


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        indexes = defaultdict(list)
        for i, c in enumerate(s):
            indexes[c].append(i)
        lengths = {
            char: get_len_set(s, indxs)
            for char, indxs in indexes.items()
            if len(indxs) >= 2
        }
        return sum(lengths.values())


def get_len_set(s: str, indexes: List) -> int:
    first, last = indexes[0], indexes[-1]
    char_set = set(s[first + 1 : last])
    return len(char_set)


solution = Solution()
assert solution.countPalindromicSubsequence("aabca") == 3
assert solution.countPalindromicSubsequence("adc") == 0
assert solution.countPalindromicSubsequence("bbcbaba") == 4
