from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        sorted_tokens = deque(sorted(tokens))
        l, r = 0, len(sorted_tokens) - 1

        while True:
            while l <= r and sorted_tokens[l] <= power:
                power -= sorted_tokens[l]
                l += 1
                score += 1
            if score >= 1 and l < r:
                power += sorted_tokens[r]
                r -= 1
                score -= 1
            else:
                break

        return score


solution = Solution()
assert solution.bagOfTokensScore([100], 50) == 0
assert solution.bagOfTokensScore([200, 100], 150) == 1
assert solution.bagOfTokensScore([100, 200, 300, 400], 200) == 2
