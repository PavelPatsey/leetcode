MIN_INT = -(2**31)
MAX_INT = 2**31 - 1


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        if len(s) == 0:
            return 0
        if i == len(s):
            return 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i >= len(s):
            return 0
        sign = "+"
        if s[i] in "+-":
            sign = s[i]
            i += 1
        sign = 1 if sign == "+" else -1
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        if not num_str:
            return 0
        num = sign * int(num_str)
        if num < MIN_INT:
            return MIN_INT
        elif num > MAX_INT:
            return MAX_INT
        return num


solution = Solution()
assert solution.myAtoi("42") == 42
assert solution.myAtoi(" -042") == -42
assert solution.myAtoi("1337c0d3") == 1337
assert solution.myAtoi("0-1") == 0
assert solution.myAtoi("words and 987") == 0
assert solution.myAtoi("-91283472332") == -2147483648
assert solution.myAtoi("") == 0
assert solution.myAtoi(" ") == 0
assert solution.myAtoi("21474836460") == 2147483647
