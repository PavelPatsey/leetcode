NUMBERS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
MIN_INT = -(2**31)
MIN_STR = str(MIN_INT)
MAX_INT = 2**31 - 1
MAX_STR = str(MAX_INT)


class Solution:
    def my_recursion(self, i: int, string: str) -> str:
        if len(string) == 0:
            return "0"
        if i >= len(string):
            return "0"
        if string[i] == " ":
            return self.my_recursion(i + 1, string)
        sign = "+"
        if string[i] in {"+", "-"}:
            sign = string[i]
            i += 1
        if i >= len(string):
            return "0"
        if string[i] in NUMBERS:
            num_list = []
            while i < len(string) and string[i] in NUMBERS:
                num_list.append(string[i])
                i += 1
            num_str = sign + "".join(num_list)
            num = int(num_str)
            if num < MIN_INT:
                num_str = MIN_STR
            elif num > MAX_INT:
                num_str = MAX_STR
            else:
                num_str = str(num)
            return num_str
        return "0"

    def myAtoi(self, s: str) -> int:
        return eval(self.my_recursion(0, s))


solution = Solution()
assert solution.myAtoi("42") == 42
assert solution.myAtoi(" -042") == -42
assert solution.myAtoi("1337c0d3") == 1337
assert solution.myAtoi("0-1") == 0
assert solution.myAtoi("words and 987") == 0
assert solution.myAtoi("-91283472332") == -2147483648
assert solution.myAtoi("") == 0
assert solution.myAtoi(" ") == 0
