class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = split(s)
        return " ".join(reversed(splitted))


def split(s: str) -> list[str]:
    res = []
    current = ""
    for r in range(len(s)):
        if s[r] != " ":
            current += s[r]
        else:
            if current:
                res.append(current)
            current = ""
    if current:
        res.append(current)
    return res


assert split("  hello world  ") == ["hello", "world"]

solution = Solution()
assert solution.reverseWords("the sky is blue") == "blue is sky the"
assert solution.reverseWords("  hello world  ") == "world hello"
