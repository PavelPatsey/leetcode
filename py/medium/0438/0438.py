from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        reference_counter = Counter(p)
        current_counter = Counter(s[0 : len(p) - 1])
        for i in range(len(s) - len(p) + 1):
            current_counter[s[i + len(p) - 1]] += 1
            if current_counter == reference_counter:
                res.append(i)
            current_counter[s[i]] -= 1
        return res


solution = Solution()
assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
