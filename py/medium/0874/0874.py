from typing import List


class Solution:
    DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    @staticmethod
    def change_index(index, command):
        new_index = index - 1 if command == -2 else index + 1
        return new_index % 4

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))
        index = 0
        point = (0, 0)
        max_distance = 0
        for command in commands:
            if command in {-1, -2}:
                index = self.change_index(index, command)
            else:
                direction = self.DIRECTIONS[index]
                i = command
                while (
                    i > 0
                    and (
                        new_coordinates := (
                            point[0] + direction[0],
                            point[1] + direction[1],
                        )
                    )
                    not in obstacles_set
                ):
                    point = new_coordinates
                    i -= 1
                max_distance = max(max_distance, sum(x * x for x in point))
        return max_distance


solution = Solution()
assert solution.change_index(0, -1) == 1
assert solution.change_index(1, -1) == 2
assert solution.change_index(2, -1) == 3
assert solution.change_index(3, -1) == 0

assert solution.change_index(0, -2) == 3
assert solution.change_index(1, -2) == 0
assert solution.change_index(2, -2) == 1
assert solution.change_index(3, -2) == 2

assert solution.robotSim([4, -1, 3], []) == 25
assert solution.robotSim([4, -1, 4, -2, 4], [[2, 4]]) == 65
assert solution.robotSim([6, -1, -1, 6], []) == 36

test_commands = [7, -2, -2, 7, 5]
test_obstacles = [
    [-3, 2],
    [-2, 1],
    [0, 1],
    [-2, 4],
    [-1, 0],
    [-2, -3],
    [0, -3],
    [4, 4],
    [-3, 3],
    [2, 2],
]
assert solution.robotSim(test_commands, test_obstacles) == 4
