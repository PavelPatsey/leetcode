from typing import List, Tuple


class Solution:
    DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    @staticmethod
    def change_index(index, command):
        new_index = index - 1 if command == -2 else index + 1
        return new_index % 4

    @staticmethod
    def transform_point(
        point: List[int],
        command: int,
        direction: Tuple[int],
        obstacles: List[List[int]],
    ) -> List[int]:
        def _is_between(x0, x1, x2):
            left, right = sorted([x0, x2])
            return left <= x1 <= right

        def get_distance(x0, x1):
            return abs(x0 - x1)

        j, i = abs(direction[0]), abs(direction[1])
        ds = direction[i] * command
        min_ds = abs(ds)
        for obstacle in obstacles:
            if obstacle[j] == point[j] and _is_between(
                point[i], obstacle[i], point[i] + ds
            ):
                min_ds = min(min_ds, get_distance(obstacle[i] - direction[i], point[i]))
        point[i] += min_ds * direction[i]
        return point

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        index = 0
        point = [0, 0]
        max_distance = 0
        for command in commands:
            if command in {-1, -2}:
                index = self.change_index(index, command)
            else:
                direction = self.DIRECTIONS[index]
                point = self.transform_point(point, command, direction, obstacles)
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
