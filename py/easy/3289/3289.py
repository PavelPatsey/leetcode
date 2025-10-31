class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        res = []
        visited = set()
        for x in nums:
            if x not in visited:
                visited.add(x)
            else:
                res.append(x)
        return res


solution = Solution()
solution.getSneakyNumbers([0, 1, 1, 0]) == [0, 1]
solution.getSneakyNumbers([0, 3, 2, 1, 3, 2]) == [2, 3]
solution.getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]) == [4, 5]
