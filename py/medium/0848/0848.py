class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        pass


def shift(char: str, x: int) -> str:
    new_ord = (ord(char) + x - ord("a")) % 26 + ord("a")
    return chr(new_ord)


assert shift("a", 1) == "b"
assert shift("z", 1) == "a"
assert shift("a", 17) == "r"
