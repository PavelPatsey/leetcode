from typing import List


class Solution:
    string = "123456789"

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def _f(k):
            a = int(self.string[:k])
            m = 10 ** (k - 1)
            subsequence = []
            for j in range(1, 10 - k + 1):
                if low <= a <= high:
                    subsequence.append(a)
                a = a % m
                a = a * 10 + j + k
            return subsequence

        result = []
        for i in range(1, 10):
            result.extend(_f(i))
        return result


solution = Solution()
assert solution.sequentialDigits(100, 300) == [123, 234]
assert solution.sequentialDigits(1000, 13000) == [
    1234,
    2345,
    3456,
    4567,
    5678,
    6789,
    12345,
]
assert solution.sequentialDigits(10, 1000000000) == [
    12,
    23,
    34,
    45,
    56,
    67,
    78,
    89,
    123,
    234,
    345,
    456,
    567,
    678,
    789,
    1234,
    2345,
    3456,
    4567,
    5678,
    6789,
    12345,
    23456,
    34567,
    45678,
    56789,
    123456,
    234567,
    345678,
    456789,
    1234567,
    2345678,
    3456789,
    12345678,
    23456789,
    123456789,
]
