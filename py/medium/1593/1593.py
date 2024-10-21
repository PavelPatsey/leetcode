from typing import List


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = 0

        def dfs(stack: List, i: int):
            if i == len(s):
                if len(stack) == len(set(stack)):
                    self.result = max(self.result, len(stack))
                return
            last_item = stack.pop()
            dfs(stack + [last_item, s[i]], i + 1)
            dfs(stack + [last_item + s[i]], i + 1)

        dfs([s[0]], 1)
        return self.result


solution = Solution()
assert solution.maxUniqueSplit("aba") == 2
assert solution.maxUniqueSplit("ababccc") == 5
assert solution.maxUniqueSplit("aa") == 1
assert solution.maxUniqueSplit("wwwzfvedwfvhsww") == 11
