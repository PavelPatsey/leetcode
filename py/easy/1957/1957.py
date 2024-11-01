class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [s[0]]
        prev_char = s[0]
        counter = 1
        for char in s[1:]:
            if char == prev_char:
                counter += 1
            else:
                prev_char = char
                counter = 1
            if counter < 3:
                result.append(char)
        return "".join(result)


solution = Solution()
assert solution.makeFancyString("l") == "l"
assert solution.makeFancyString("leeetcode") == "leetcode"
assert solution.makeFancyString("aaabaaaa") == "aabaa"
assert solution.makeFancyString("aab") == "aab"
