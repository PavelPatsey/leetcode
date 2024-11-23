from typing import List


class Solution:
    @staticmethod
    def _convert(row: List[str]) -> List[str]:
        stone = "#"
        obstacle = "*"
        empty = "."
        converted = []
        stone_number = empty_number = 0
        for item in row:
            if item == obstacle:
                converted.extend(
                    [empty] * empty_number + [stone] * stone_number + [obstacle]
                )
                stone_number = empty_number = 0
            elif item == stone:
                stone_number += 1
            elif item == empty:
                empty_number += 1
            else:
                raise Exception("Error in else case!")
        converted.extend([empty] * empty_number + [stone] * stone_number)
        return converted

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        converted_box = [self._convert(row) for row in box]
        rotated = [list(x) for x in zip(*[row for row in converted_box][::-1])]
        return rotated


solution = Solution()
assert solution.rotateTheBox([["#", ".", "#"]]) == [
    ["."],
    ["#"],
    ["#"],
]

assert solution.rotateTheBox(
    [
        ["#", ".", "*", "."],
        ["#", "#", "*", "."],
    ]
) == [
    ["#", "."],
    ["#", "#"],
    ["*", "*"],
    [".", "."],
]

assert solution.rotateTheBox(
    [
        ["#", "#", "*", ".", "*", "."],
        ["#", "#", "#", "*", ".", "."],
        ["#", "#", "#", ".", "#", "."],
    ]
) == [
    [".", "#", "#"],
    [".", "#", "#"],
    ["#", "#", "*"],
    ["#", "*", "."],
    ["#", ".", "*"],
    ["#", ".", "."],
]
