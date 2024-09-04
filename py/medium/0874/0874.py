from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple, obstacles))
        x, y = 0, 0
        dx, dy = 0, 1
        max_distance = 0
        for command in commands:
            if command == -2:
                dx, dy = -dy, dx
            elif command == -1:
                dx, dy = dy, -dx
            else:
                i = command
                while i > 0 and (new_point := (x + dx, y + dy)) not in obstacles_set:
                    x, y = new_point
                    i -= 1
                max_distance = max(max_distance, x * x + y * y)
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
