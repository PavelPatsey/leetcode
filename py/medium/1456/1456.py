class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        counter = 0
        for char in s[:k]:
            if char in vowels:
                counter += 1
        res = counter
        l, r = 1, k
        while r < len(s):
            if s[l - 1] in vowels:
                counter -= 1
            if s[r] in vowels:
                counter += 1
            res = max(res, counter)
            l += 1
            r += 1
        return res


solution = Solution()
assert solution.maxVowels("abciiidef", 3) == 3
assert solution.maxVowels("a", 1) == 1
