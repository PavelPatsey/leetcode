from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five >= 1:
                    five -= 1
                else:
                    return False
            elif bill == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            else:
                assert False
        return True


solution = Solution()
assert solution.lemonadeChange([5, 5, 5, 10, 20]) is True
assert solution.lemonadeChange([5, 5, 10, 10, 20]) is False
