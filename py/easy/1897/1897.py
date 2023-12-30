from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            counter.update(word)

        len_words = len(words)
        for value in counter.values():
            if value % len_words != 0:
                return False
        return True


solution = Solution()
assert solution.makeEqual(words=["abc", "aabc", "bc"]) is True
assert solution.makeEqual(words=["ab", "a"]) is False
