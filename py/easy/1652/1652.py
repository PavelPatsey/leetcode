from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        if k == 0:
            return [0] * N
        elif k > 0:
            array = code + code
            n = k
            start, end, step = 0, N, 1
        else:
            array = (code + code)[::-1]
            n = -k
            start, end, step = N - 1, -1, -1
        return [sum(array[i + 1 : i + n + 1]) for i in range(start, end, step)]


solution = Solution()
assert solution.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
assert solution.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
assert solution.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
