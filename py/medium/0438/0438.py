from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        counter_p = Counter(p)
        print(counter_p)
        res = []
        for i in range(len(s) - len(p) + 1):
            current_counter = Counter(s[i : i + len(p)])
            if current_counter == counter_p:
                res.append(i)
        print(f"{res=}")
        return res


solution = Solution()
assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
assert solution.findAnagrams("abab", p="ab") == [0, 1, 2]
