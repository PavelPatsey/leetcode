class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        arr_set = set(arr)
        res = 0

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                while nxt in arr_set:
                    length += 1
                    prev, cur = cur, nxt
                    nxt = prev + cur
                    res = max(res, length)

        return res


solution = Solution()
assert solution.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5
assert solution.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]) == 3
assert solution.lenLongestFibSubseq([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]) == 5
