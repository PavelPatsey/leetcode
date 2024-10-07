class Solution:
    def minLength(self, s: str) -> int:
        string = s
        i = 0
        while i < len(string) - 1:
            if (
                string[i] == "A"
                and string[i + 1] == "B"
                or string[i] == "C"
                and string[i + 1] == "D"
            ):
                string = string[:i] + string[i + 2 :]
                i = 0
            else:
                i += 1
        return len(string)


solution = Solution()
assert solution.minLength("FC") == 2
assert solution.minLength("ABFCACDB") == 2
assert solution.minLength("ACBBD") == 5
