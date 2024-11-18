from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        if k == 0:
            return [0] * N
        elif k > 0:
            ext_code = code + code
            result = [sum(ext_code[i + 1 : i + k + 1]) for i in range(N)]
        else:
            rev_ext_code = (code + code)[::-1]
            k = -k
            result = [
                sum(rev_ext_code[i + 1 : i + k + 1]) for i in range(N - 1, -1, -1)
            ]
        return result


solution = Solution()
assert solution.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
assert solution.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
assert solution.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
