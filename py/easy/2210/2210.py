class Solution:
    @staticmethod
    def remove_duplicates(nums: list[int]) -> list[int]:
        if not nums:
            return []
        result = [nums[0]]
        for x, y in zip(nums, nums[1:]):
            if x != y:
                result.append(y)
        return result

    def countHillValley(self, nums: list[int]) -> int:
        removed = self.remove_duplicates(nums)
        counter = 0
        for x, y, z in zip(removed, removed[1:], removed[2:]):
            if x < y > z:
                counter += 1
            if x > y < z:
                counter += 1
        return counter


solution = Solution()
assert solution.remove_duplicates([2, 4, 1, 1, 6, 5]) == [2, 4, 1, 6, 5]
assert solution.remove_duplicates([6, 6, 5, 5, 4, 1]) == [6, 5, 4, 1]
assert solution.remove_duplicates([1, 1, 1]) == [1]
assert solution.remove_duplicates([1, 1]) == [1]
assert solution.remove_duplicates([2, 1, 1]) == [2, 1]
assert solution.remove_duplicates([]) == []


assert solution.countHillValley([2, 4, 1, 1, 6, 5]) == 3
assert solution.countHillValley([6, 6, 5, 5, 4, 1]) == 0
