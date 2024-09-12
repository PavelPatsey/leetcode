from typing import List
from functools import reduce


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def _is_allowed_string(string: str):
            string_set = set(string)
            return all((char in allowed for char in string_set))

        filtered = filter(_is_allowed_string, words)
        return reduce(lambda acc, x: acc + 1, filtered, 0)


solution = Solution()
assert solution.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2
assert (
    solution.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"])
    == 7
)
