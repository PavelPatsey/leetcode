from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        frequency_word1 = Counter(word1)
        frequency_word2 = Counter(word2)

        keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())
        if not keys_match:
            return False

        sorted_values_word1 = sorted(frequency_word1.values())
        sorted_values_word2 = sorted(frequency_word2.values())
        return sorted_values_word1 == sorted_values_word2


solution = Solution()
assert solution.closeStrings("abc", "bca") is True
assert solution.closeStrings("a", "aa") is False
assert solution.closeStrings("cabbba", "abbccc") is True
assert solution.closeStrings("uau", "ssx") is False
