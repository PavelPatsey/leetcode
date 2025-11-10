class Solution:
    def compress(self, chars: list[str]) -> int:
        l = 0
        r = 0
        i = 0
        while r < len(chars):
            while r < len(chars) and chars[r] == chars[l]:
                r += 1
            chars[i] = chars[l]
            i += 1
            length = r - l
            if length > 1:
                for c in str(length):
                    chars[i] = c
                    i += 1
            l = r
        return i


solution = Solution()
assert solution.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
