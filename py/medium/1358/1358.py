import math


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        counter = {"a": 0, "b": 0, "c": 0}
        counter[s[left]] += 1
        while left <= right < len(s):
            if math.prod(counter.values()) == 0:
                right += 1
                if right < len(s):
                    counter[s[right]] += 1
            elif math.prod(counter.values()) != 0:
                counter[s[left]] -= 1
                left += 1
                res += len(s) - right
            else:
                assert False
        return res


solution = Solution()
assert solution.numberOfSubstrings("abcabc") == 10
assert solution.numberOfSubstrings("aaacb") == 3
assert solution.numberOfSubstrings("ababbbc") == 3
