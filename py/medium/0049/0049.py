from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = defaultdict(list)
        for word in strs:
            words_dict["".join(sorted(word))].append(word)
        return list(words_dict.values())


solution = Solution()
assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"],
]
assert solution.groupAnagrams([""]) == [[""]]
assert solution.groupAnagrams(["a"]) == [["a"]]
