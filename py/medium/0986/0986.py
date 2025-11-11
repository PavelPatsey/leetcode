class Solution:
    def intervalIntersection(
        self, firstlist: list[list[int]], secondlist: list[list[int]]
    ) -> list[list[int]]:
        res = []
        i = 0
        j = 0
        while i < len(firstlist) and j < len(secondlist):
            a = firstlist[i]
            b = secondlist[j]
            if is_intersect(a, b):
                res.append(intersection(a, b))
            if a[1] < b[1]:
                i += 1
            else:
                j += 1
        return res


def is_intersect(a: list, b: list) -> bool:
    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]


def intersection(a: list, b: list) -> list:
    return [max(a[0], b[0]), min(a[1], b[1])]


solution = Solution()

assert solution.intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]],
    [[1, 5], [8, 12], [15, 24], [25, 26]],
) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

assert solution.intervalIntersection([[1, 3], [5, 9]], []) == []
