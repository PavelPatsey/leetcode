from collections import deque
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        q = deque(spaces)
        index = q.popleft()
        for i, char in enumerate(s):
            if i == index:
                res.append(" ")
                if q:
                    index = q.popleft()
            res.append(char)
        return "".join(res)


solution = Solution()
assert (
    solution.addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]) == "Leetcode Helps Me Learn"
)
