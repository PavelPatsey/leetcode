from typing import List
from itertools import chain
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(f % len(words) == 0 for f in Counter(chain(*words)).values())


solution = Solution()

solution.makeEqual(words=["abc", "aabc", "bc"]) is True
solution.makeEqual(words=["ab","a"]) is False
