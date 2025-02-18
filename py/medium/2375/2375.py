from typing import List, Optional


class Solution:
    results = set()

    @staticmethod
    def find_larger_nums(n: int, nums: set, pattern: str) -> set:
        if pattern == "I":
            result = set(filter(lambda x: x > n, nums))
        elif pattern == "D":
            result = set(filter(lambda x: x < n, nums))
        else:
            assert False
        return result

    @staticmethod
    def find_smaller_nums(n: int, nums: set) -> set:
        return set(filter(lambda x: x < n, nums))

    def do_smallest_number(self, n: int, nums: set, pat_list: List[str], res: str):
        if len(pat_list) == 0:
            self.results.add(res)
            return
        pattern = pat_list[0]
        for i in self.find_larger_nums(n, nums, pattern):
            self.do_smallest_number(i, nums - {i}, pat_list[1:], res + str(i))

    def smallestNumber(self, pattern: str) -> Optional[str]:
        self.results = set()
        nums_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in nums_lst:
            self.do_smallest_number(i, set(nums_lst) - {i}, list(pattern), str(i))
            if self.results:
                return sorted(self.results)[0]


solution = Solution()
assert solution.smallestNumber("IIIDIDDD") == "123549876"
assert solution.smallestNumber("DDD") == "4321"
