from collections import OrderedDict
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct_strings = OrderedDict()
        for char in arr:
            if char not in distinct_strings:
                distinct_strings[char] = 1
            else:
                distinct_strings[char] += 1

        counter = 0
        for key, value in distinct_strings.items():
            if value == 1:
                counter += 1
            if counter == k:
                return key
        return ""


solution = Solution()
assert solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2) == "a"
assert solution.kthDistinct(["aaa", "aa", "a"], 1) == "aaa"
assert solution.kthDistinct(["a", "b", "a"], 3) == ""
