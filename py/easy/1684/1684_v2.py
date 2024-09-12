from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0

        for word in words:
            for char in word:
                if char not in allowed_set:
                    count += 1
                    break

        return len(words) - count


solution = Solution()
assert solution.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2
assert (
    solution.countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"])
    == 7
)
