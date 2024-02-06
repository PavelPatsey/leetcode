from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        ord_a = ord("a")
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord_a] += 1
            result[tuple(count)].append(word)
        return list(result.values())


solution = Solution()
assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"],
]
assert solution.groupAnagrams([""]) == [[""]]
assert solution.groupAnagrams(["a"]) == [["a"]]
