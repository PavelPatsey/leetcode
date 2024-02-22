from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        nodes = defaultdict(int)
        children = defaultdict(int)
        for node, child in trust:
            nodes[node] += 1
            children[child] += 1

        for i in range(1, n + 1):
            if nodes[i] == 0 and children[i] == n - 1:
                return i
        return -1


solutions = Solution()
assert solutions.findJudge(2, [[1, 2]]) == 2
assert solutions.findJudge(3, [[1, 3], [2, 3]]) == 3
assert solutions.findJudge(2, [[1, 3], [2, 3], [3, 1]]) == -1
assert solutions.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
