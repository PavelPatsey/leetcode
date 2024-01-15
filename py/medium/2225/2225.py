from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        [winners, losers] = list(zip(*matches))
        counter_losers = Counter(losers)

        players = set(chain(winners, losers))
        answer = [[], []]

        for player in players:
            if player not in counter_losers:
                answer[0].append(player)
            if player in counter_losers and counter_losers[player] == 1:
                answer[1].append(player)
        return [sorted(answer[0]), sorted(answer[1])]


solution = Solution()
assert solution.findWinners(
    [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
) == [[1, 2, 10], [4, 5, 7, 8]]
assert solution.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []]
