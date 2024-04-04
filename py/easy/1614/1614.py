class Solution:
    def maxDepth(self, s: str) -> int:
        current_counter = max_counter = 0
        for char in s:
            if char == "(":
                current_counter += 1
                max_counter = max(max_counter, current_counter)
            elif char == ")":
                current_counter -= 1

        return max_counter


solution = Solution()
assert solution.maxDepth("(1+(2*3)+((8)/4))+1") == 3
assert solution.maxDepth("(1)+((2))+(((3)))") == 3
