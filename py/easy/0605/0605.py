class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        counter = 0
        i = 0
        while i < len(flowerbed) and counter < n:
            if flowerbed[i] == 0:
                empty_left = i == 0 or flowerbed[i - 1] == 0
                empty_right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    counter += 1
            i += 1
        return counter >= n


solution = Solution()
assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
assert solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False
assert solution.canPlaceFlowers([0, 0, 1, 0, 1], 1) == True
assert solution.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0) == True
