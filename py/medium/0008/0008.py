MIN_INT = -(2**31)
MAX_INT = 2**31 - 1


class Solution:
    @staticmethod
    def is_number(char: str):
        return ord("0") <= ord(char) <= ord("9")

    def myAtoi(self, s: str) -> int:
        string = s
        i = 0
        if len(string) == 0:
            return 0
        if i >= len(string):
            return 0
        if string[i] == " ":
            while i < len(string) and string[i] == " ":
                i += 1
        if i >= len(string):
            return 0
        sign = "+"
        if string[i] in {"+", "-"}:
            sign = string[i]
            i += 1
        if i >= len(string):
            return 0
        if self.is_number(string[i]):
            num_list = []
            while i < len(string) and self.is_number(string[i]):
                num_list.append(string[i])
                i += 1
            num_str = sign + "".join(num_list)
            num = int(num_str)
            if num < MIN_INT:
                return MIN_INT
            elif num > MAX_INT:
                return MAX_INT
            else:
                return num
        return 0


solution = Solution()
assert solution.myAtoi("42") == 42
assert solution.myAtoi(" -042") == -42
assert solution.myAtoi("1337c0d3") == 1337
assert solution.myAtoi("0-1") == 0
assert solution.myAtoi("words and 987") == 0
assert solution.myAtoi("-91283472332") == -2147483648
assert solution.myAtoi("") == 0
assert solution.myAtoi(" ") == 0
