from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for x in arr2:
            part = [y for y in arr1 if y == x]
            result.extend(part)
        part = [y for y in arr1 if y not in arr2]
        part.sort()
        result.extend(part)
        return result


solution = Solution()
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
assert solution.relativeSortArray(arr1, arr2) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
assert solution.relativeSortArray(arr1, arr2) == [22, 28, 8, 6, 17, 44]
