from itertools import pairwise
from math import prod
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lst = [string.count("1") for string in bank if "1" in string]
        return sum(map(prod, pairwise(lst)))


solution = Solution()
assert solution.numberOfBeams(["011001", "000000", "010100", "001000"]) == 8
assert solution.numberOfBeams(["000", "111", "000"]) == 0
