from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        N = len(code)
        for i in range(N):
            s = 0
            if k > 0:
                for j in range(1, k + 1):
                    s += code[(i + j) % N]
                result.append(s)
            elif k < 0:
                for j in range(-1, k - 1, -1):
                    s += code[(i + j) % N]
                result.append(s)
            else:
                result.append(0)
        return result


solution = Solution()
assert solution.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
assert solution.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
assert solution.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
