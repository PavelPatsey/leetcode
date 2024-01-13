from functools import reduce


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def _get_vowels_count(string: str) -> int:
            vowels = set("aeiouAEIOU")
            filtered = filter(lambda x: x in vowels, string)
            return reduce(lambda acc, x: acc + 1, filtered, 0)

        n = len(s) // 2
        return _get_vowels_count(s[:n]) == _get_vowels_count(s[n:])


solution = Solution()

assert solution.halvesAreAlike("book") is True
assert solution.halvesAreAlike("textbook") is False
