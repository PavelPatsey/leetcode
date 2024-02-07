from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join((k * v for k, v in Counter(s).most_common()))


solution = Solution()
assert solution.frequencySort("tree") == "eetr"
assert solution.frequencySort("cccaaa") == "cccaaa"
assert solution.frequencySort("Aabb") == "bbAa"
