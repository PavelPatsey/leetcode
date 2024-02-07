from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        buckets = defaultdict(list)
        for char, freq in Counter(s).items():
            buckets[freq].append(char)
        result = ""
        for i in range(len(s), 0, -1):
            for char in buckets[i]:
                result += char * i
        return result


solution = Solution()
assert solution.frequencySort("tree") == "eetr"
assert solution.frequencySort("cccaaa") == "cccaaa"
assert solution.frequencySort("Aabb") == "bbAa"
