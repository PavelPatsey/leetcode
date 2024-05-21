from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result


solution = Solution()
sol = solution.subsets([1, 2, 3])
answer = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
assert {tuple(x) for x in sol} == {tuple(x) for x in answer}
