class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = {"a": 0, "b": 0, "c": 0}
        for char in s:
            counter[char] += 1

        if min(counter.values()) < k:
            return -1

        res = float("inf")
        l = 0
        for r in range(len(s)):
            counter[s[r]] -= 1

            while min(counter.values()) < k:
                counter[s[l]] += 1
                l += 1
            res = min(res, len(s) - (r - l + 1))
        return res


solution = Solution()
assert solution.takeCharacters("aabbcc", 2) == 6
assert solution.takeCharacters("aabaaaacaabc", 2) == 8
assert solution.takeCharacters("a", 1) == -1
assert solution.takeCharacters("a", 0) == 0
