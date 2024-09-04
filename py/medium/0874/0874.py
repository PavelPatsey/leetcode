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
        if direction in {(1, 0), (-1, 0)}:
            i, j = 0, 1
        else:
            i, j = 1, 0
        ds = direction[i] * command
        min_ds = abs(ds)
        for obstacle in obstacles:
            if obstacle[j] == point[j] and point[i] <= obstacle[i] <= point[i] + ds:
                min_ds = min(ds, abs(obstacle[i] - direction[i]))
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
assert (
    solution.robotSim(
        [7, -2, -2, 7, 5],
        [
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
        ],
    )
    == 4
)
