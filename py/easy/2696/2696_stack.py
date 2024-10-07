class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char == "B" and stack[-1] == "A" or char == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)


solution = Solution()
assert solution.minLength("D") == 1
assert solution.minLength("FC") == 2
assert solution.minLength("ABFCACDB") == 2
assert solution.minLength("ACBBD") == 5
