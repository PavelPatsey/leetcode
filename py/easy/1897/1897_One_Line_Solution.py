from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return not any(f % len(words) for f in Counter(chain(*words)).values())


solution = Solution()
assert solution.makeEqual(words=["abc", "aabc", "bc"]) is True
assert solution.makeEqual(words=["ab", "a"]) is False
