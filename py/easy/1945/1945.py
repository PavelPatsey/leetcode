class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def _convert_string(string: str) -> int:
            return int("".join([str(ord(char) - ord("a") + 1) for char in string]))

        def _transform_number(number: int) -> int:
            number_str = str(number)
            chars = (char for char in number_str)
            return sum(map(int, chars))

        result = _convert_string(s)
        while k != 0:
            result = _transform_number(result)
            k -= 1
        return result


solution = Solution()
assert solution.getLucky("iiii", 1) == 36
assert solution.getLucky("leetcode", 2) == 6
assert solution.getLucky("zbax", 2) == 8
