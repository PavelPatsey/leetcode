from operator import itemgetter
from typing import List

CATEGORIES = ["electronics", "grocery", "pharmacy", "restaurant"]


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        zipped = zip(code, businessLine, isActive)
        filtered = filter(lambda x: is_valid(*x), zipped)
        sorted_filtered = sorted(filtered, key=itemgetter(1, 0))
        return [x[0] for x in sorted_filtered]


def valid_code(code: str) -> bool:
    if not code:
        return False
    for ch in code:
        if not (ch.isalpha() or ch.isdigit() or ch == "_"):
            return False
    return True


def is_valid(code, business_line, is_active) -> bool:
    return valid_code(code) and business_line in CATEGORIES and is_active


solution = Solution()
assert solution.validateCoupons(
    code=["SAVE20", "", "PHARMA5", "SAVE@20"],
    businessLine=["restaurant", "grocery", "pharmacy", "restaurant"],
    isActive=[True, True, True, True],
) == ["PHARMA5", "SAVE20"]

assert solution.validateCoupons(
    code=["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
    businessLine=["grocery", "electronics", "invalid"],
    isActive=[False, True, True],
) == ["ELECTRONICS_50"]
