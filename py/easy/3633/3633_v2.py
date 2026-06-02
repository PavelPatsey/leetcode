class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        def calc_time(
            start1: list[int], dur1: list[int], start2: list[int], dur2: list[int]
        ) -> int:
            e1 = float("inf")
            for s1, d1 in zip(start1, dur1):
                e1 = min(e1, s1 + d1)
            e2 = float("inf")
            for s2, d2 in zip(start2, dur2):
                e2 = min(e2, max(e1, s2) + d2)
            return e2

        time1 = calc_time(landStartTime, landDuration, waterStartTime, waterDuration)
        time2 = calc_time(waterStartTime, waterDuration, landStartTime, landDuration)
        res = min(time1, time2)
        return res


solution = Solution()
assert solution.earliestFinishTime([2, 8], [4, 1], [6], [3]) == 9
assert solution.earliestFinishTime([5], [3], [1], [10]) == 14
