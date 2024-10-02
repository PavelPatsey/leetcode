from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_dict = {value: key + 1 for key, value in enumerate(sorted(set(arr)))}
        return [rank_dict[x] for x in arr]


solution = Solution()
assert solution.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]
