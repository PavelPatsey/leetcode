import re
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        pattern = r"[+-]?\d+/\d+"
        exp_list = re.findall(pattern, expression)

        numerals = []
        denominators = []
        for exp in exp_list:
            splitted = exp.split("/")
            numerals.append(int(splitted[0]))
            denominators.append(int(splitted[1]))

        common_denominator = math.lcm(*denominators)
        numeral_list = [
            n * common_denominator / d for n, d in zip(numerals, denominators)
        ]
        numeral_sum = int(sum(numeral_list))

        numeral = numeral_sum
        denominator = common_denominator

        if numeral != 0:
            gcd = math.gcd(numeral, denominator)
            numeral = numeral // gcd
            denominator = denominator // gcd
            answer = str(numeral) + "/" + str(denominator)
        else:
            answer = "0/1"

        return answer


solution = Solution()
assert solution.fractionAddition("-1/2+1/2") == "0/1"
assert solution.fractionAddition("-1/2+1/2+1/3") == "1/3"
assert solution.fractionAddition("1/3-1/2") == "-1/6"
