class Solution:
    def reverseParentheses(self, s: str) -> str:
        string = []
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                s = stack.pop()
                string[s:i] = string[s:i][::-1]
            string.append(c)
        return "".join(c for c in string if c.isalpha())


solution = Solution()
assert solution.reverseParentheses("(abcd)") == "dcba"
assert solution.reverseParentheses("(u(love)i)") == "iloveu"
