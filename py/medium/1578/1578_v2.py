class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0
        i = 0
        while i < len(colors):
            j = 1
            dt = 0
            min_t = neededTime[i]
            while i + j < len(colors) and colors[i] == colors[i + j]:
                if neededTime[i + j] < min_t:
                    dt += neededTime[i + j]
                else:
                    dt += min_t
                    min_t = neededTime[i + j]
                j += 1
            res += dt
            i += j
        return res


solution = Solution()
assert solution.minCost("abaac", [1, 2, 3, 4, 5]) == 3
assert solution.minCost("abc", [1, 2, 3]) == 0
assert solution.minCost("aabaa", [1, 2, 3, 4, 1]) == 2
assert solution.minCost("abbbbba", [1, 2, 3, 4, 5, 6, 7]) == 14
assert solution.minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]) == 26
