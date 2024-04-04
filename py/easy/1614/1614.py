class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = max_depth = 0
        for char in s:
            if char == "(":
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ")":
                current_depth -= 1

        return max_depth


solution = Solution()
assert solution.maxDepth("(1+(2*3)+((8)/4))+1") == 3
assert solution.maxDepth("(1)+((2))+(((3)))") == 3
