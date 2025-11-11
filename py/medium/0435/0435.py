from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        sorted_vals = sorted(intervals, key=itemgetter(1))
        cur_val = sorted_vals[0]
        counter = 0
        for i in range(1, len(sorted_vals)):
            if intersect(cur_val, sorted_vals[i]):
                counter += 1
            else:
                cur_val = sorted_vals[i]
        return counter


def intersect(a: list[int], b: list[int]) -> bool:
    return a[1] > b[0]


solution = Solution()
assert solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
