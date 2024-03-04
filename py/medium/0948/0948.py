from collections import deque
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        sorted_tokens = deque(sorted(tokens))

        while sorted_tokens:
            if sorted_tokens[0] <= power:
                power -= sorted_tokens.popleft()
                score += 1
                continue
            if score >= 1 and len(sorted_tokens) >= 2:
                power += sorted_tokens.pop()
                score -= 1
            else:
                break

        return score


solution = Solution()
assert solution.bagOfTokensScore([100], 50) == 0
assert solution.bagOfTokensScore([200, 100], 150) == 1
assert solution.bagOfTokensScore([100, 200, 300, 400], 200) == 2
