class Solution:
    def compress(self, chars: list[str]) -> int:
        prev = chars[0]
        counter = 1
        l = 0
        for i in range(1, len(chars)):
            if chars[i] == prev:
                counter += 1
            else:
                chars[l] = prev
                l += 1
                if counter > 1:
                    for c in str(counter):
                        chars[l] = c
                        l += 1
                counter = 1
            prev = chars[i]
        chars[l] = prev
        l += 1
        if counter > 1:
            for c in str(counter):
                chars[l] = c
                l += 1
        return l


solution = Solution()
assert solution.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
