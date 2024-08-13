from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def _get_list_of_unique_lists(
            list_of_lists: List[List[int]],
        ) -> List[List[int]]:
            return [
                item
                for i, item in enumerate(list_of_lists)
                if item not in list_of_lists[:i]
            ]

        result = []
        sorted_candidates = sorted(candidates)

        def dfs(i, sub_list):
            if sum(sub_list) == target:
                result.append(sub_list)
                return
            if sum(sub_list) > target:
                return
            if i >= len(sorted_candidates):
                return
            dfs(i + 1, sub_list + [sorted_candidates[i]])
            dfs(i + 1, sub_list.copy())

        dfs(0, [])
        return _get_list_of_unique_lists(result)


solution = Solution()
assert solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
    [1, 1, 6],
    [1, 2, 5],
    [1, 7],
    [2, 6],
]

assert solution.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
