from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        participants = set(range(n))
        children = {ch for _, ch in edges}
        parents = participants - children
        return list(parents)[0] if len(parents) == 1 else -1


solution = Solution()
assert solution.findChampion(3, [[0, 1], [1, 2]]) == 0
assert solution.findChampion(4, [[0, 2], [1, 3], [1, 2]]) == -1
assert solution.findChampion(1, []) == 0
assert solution.findChampion(2, [[1, 0]]) == 1
