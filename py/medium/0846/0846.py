from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        sorted_hand = sorted(hand)
        i = 0
        current_group = []
        while sorted_hand and i < len(sorted_hand):
            if not current_group:
                current_group.append(sorted_hand[i])
                del sorted_hand[i]
            elif current_group[-1] == sorted_hand[i]:
                i += 1
            elif current_group[-1] + 1 == sorted_hand[i]:
                current_group.append(sorted_hand[i])
                del sorted_hand[i]
            else:
                return False
            if len(current_group) == groupSize:
                current_group = []
                i = 0
        return True if not current_group else False


solution = Solution()
assert solution.isNStraightHand([1, 2, 3], 3) is True
assert solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
assert solution.isNStraightHand([1, 2, 3, 4, 5], 4) is False
assert solution.isNStraightHand([1, 2, 3, 2, 3, 4], 3) is True
assert solution.isNStraightHand([1, 1, 2, 2, 3, 3], 3) is True
assert solution.isNStraightHand([1, 1, 2, 2, 3, 3], 2) is False
