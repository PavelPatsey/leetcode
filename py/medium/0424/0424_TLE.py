from collections import Counter


class Solution:
    @staticmethod
    def needed_permutations(s: str):
        counter = Counter(s)
        return sum(counter.values()) - max(counter.values())

    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        while left < len(s):
            right = left + 1
            while right <= len(s) and self.needed_permutations(s[left:right]) <= k:
                right += 1
            res = max(right - left - 1, res)
            left += 1
        return res


solution = Solution()
assert solution.characterReplacement("ABAB", 2) == 4
assert solution.characterReplacement("AABABBA", 1) == 4
assert solution.characterReplacement("A", 0) == 1
assert solution.characterReplacement("A", 1) == 1
assert solution.characterReplacement("ABBB", 2) == 4


assert solution.needed_permutations("ab") == 1
assert solution.needed_permutations("aba") == 1
assert solution.needed_permutations("abaa") == 1
assert solution.needed_permutations("abc") == 2
assert solution.needed_permutations("a") == 0
