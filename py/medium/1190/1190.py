class Solution:
    def reverseParentheses(self, s: str) -> str:
        def _find_indexes(string):
            i = 0
            right = left = None
            while i < len(string) and left is None:
                if string[i] == "(":
                    right = i
                elif string[i] == ")":
                    left = i
                i += 1
            return right, left if (right is not None and left is not None) else None

        def _get_new_string(string, right, left):
            return (
                string[0:right]
                + string[right + 1 : left][::-1]
                + string[left + 1 : len(s)]
            )

        while any((char in {"(", ")"}) for char in s):
            r, l = _find_indexes(s)
            s = _get_new_string(s, r, l)
        return s


solution = Solution()
assert solution.reverseParentheses("(abcd)") == "dcba"
assert solution.reverseParentheses("(u(love)i)") == "iloveu"
