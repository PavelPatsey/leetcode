class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for char_s, char_t in zip(s, t):
            if char_s not in dict_s:
                dict_s[char_s] = char_t
            else:
                if dict_s[char_s] != char_t:
                    return False
            if char_t not in dict_t:
                dict_t[char_t] = char_s
            else:
                if dict_t[char_t] != char_s:
                    return False
        return True


solution = Solution()
assert solution.isIsomorphic("egg", "add") is True
assert solution.isIsomorphic("foo", "bar") is False
assert solution.isIsomorphic("paper", "title") is True
assert solution.isIsomorphic("badc", "baba") is False
