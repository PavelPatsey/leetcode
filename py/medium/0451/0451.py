from collections import Counter
from operator import itemgetter


class Solution:
    def frequencySort(self, s: str) -> str:
        sorted_list = sorted(Counter(s).items(), key=itemgetter(1), reverse=True)
        result = [item[0] * item[1] for item in sorted_list]
        return "".join(result)


solution = Solution()
assert solution.frequencySort("tree") == "eetr"
assert solution.frequencySort("cccaaa") == "cccaaa"
assert solution.frequencySort("Aabb") == "bbAa"
