class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if char == "(":
                stack.append(char)
                count += 1
            elif stack:
                stack.pop()
                count -= 1
            else:
                count += 1
        return count


solution = Solution()
assert solution.minAddToMakeValid("()") == 0
assert solution.minAddToMakeValid("(") == 1
assert solution.minAddToMakeValid(")") == 1
assert solution.minAddToMakeValid("())") == 1
assert solution.minAddToMakeValid("(((") == 3
assert solution.minAddToMakeValid("()))") == 2
