class Solution:
    @staticmethod
    def _merge_two_sorted_nums(nums1, nums2):
        lst = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                lst.append(nums1[i])
                i += 1
            else:
                lst.append(nums2[j])
                j += 1
        lst.extend(nums1[i:])
        lst.extend(nums2[j:])
        return lst

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_list = self._merge_two_sorted_nums(nums1[:m], nums2)
        for i, n in enumerate(merged_list):
            nums1[i] = n


solution = Solution()

nums_1 = [1, 2, 3, 0, 0, 0]
solution.merge(nums1=nums_1, m=3, nums2=[2, 5, 6], n=3)
assert nums_1 == [1, 2, 2, 3, 5, 6]

nums_1 = [1]
solution.merge(nums1=nums_1, m=1, nums2=[], n=0)
assert nums_1 == [1]

nums_1 = [0]
solution.merge(nums1=nums_1, m=0, nums2=[1], n=1)
assert nums_1 == [1]
