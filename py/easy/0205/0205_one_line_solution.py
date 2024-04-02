class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


solution = Solution()
assert solution.isIsomorphic("egg", "add") is True
assert solution.isIsomorphic("foo", "bar") is False
assert solution.isIsomorphic("paper", "title") is True
assert solution.isIsomorphic("badc", "baba") is False
