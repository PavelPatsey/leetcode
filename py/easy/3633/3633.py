def calc_duration(ls: int, ld: int, ws: int, wd: int) -> int:
    if ls < ws:
        e1 = ls + ld
        s2 = max(e1, ws)
        res = s2 + wd
    else:
        e1 = ws + wd
        s2 = max(e1, ls)
        res = s2 + ld
    return res


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        res = 1_000_000
        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                res = min(res, calc_duration(ls, ld, ws, wd))
        return res


solution = Solution()
assert solution.earliestFinishTime([2, 8], [4, 1], [6], [3]) == 9
assert solution.earliestFinishTime([5], [3], [1], [10]) == 14
