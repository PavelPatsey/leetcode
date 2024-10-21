from typing import List


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result_list = []

        def dfs(stack: List, i: int):
            if i == len(s):
                print(stack)
                result_list.append(len(stack))
                return stack
            last_item = stack.pop()
            if s[i] not in stack and s[i] != last_item:
                dfs(stack + [last_item, s[i]], i + 1)
            elif last_item + s[i] not in stack:
                dfs(stack + [last_item + s[i]], i + 1)

        dfs([s[0]], 1)
        print(result_list)
        return max(result_list)


solution = Solution()
assert solution.maxUniqueSplit("aba") == 2
assert solution.maxUniqueSplit("ababccc") == 5
assert solution.maxUniqueSplit("aa") == 1
assert solution.maxUniqueSplit("wwwzfvedwfvhsww") == 11
