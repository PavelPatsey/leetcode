class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total = 0
        shifted = []
        for x, char in zip(reversed(shifts), reversed(s)):
            total += x
            shifted.append(shift(char, total))
        return "".join(shifted[::-1])


def shift(char: str, x: int) -> str:
    new_ord = (ord(char) + x - ord("a")) % 26 + ord("a")
    return chr(new_ord)


assert shift("a", 1) == "b"
assert shift("z", 1) == "a"
assert shift("a", 17) == "r"


solution = Solution()
assert solution.shiftingLetters("abc", [3, 5, 9]) == "rpl"
