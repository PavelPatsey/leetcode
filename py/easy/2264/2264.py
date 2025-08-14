class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev_char = num[0]
        max_char = ""
        counter = 0
        for char in num[1:]:
            if char == prev_char:
                counter += 1
            else:
                if counter >= 2 and prev_char > max_char:
                    max_char = prev_char
                counter = 0
            prev_char = char
        if counter >= 2 and prev_char > max_char:
            max_char = prev_char
        return max_char * 3


solution = Solution()
assert solution.largestGoodInteger("6777133339") == "777"
assert solution.largestGoodInteger("2300019") == "000"
assert solution.largestGoodInteger("42352338") == ""
assert solution.largestGoodInteger("222") == "222"
