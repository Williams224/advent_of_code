# main
# Tail
# Head (Tail)
# Head-> Apply Move
# Tail ->Update

from pprint import pprint
import numpy as np


class Knot:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.position_history = []

    def process_instruction(self, instruction):
        direction = instruction.split(" ")[0]
        distance = int(instruction.split(" ")[1])
        return direction, distance

    def _step(self, direction):
        print(f"stepping in _step {self.name}")
        if direction == "L":
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == "R":
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "U":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "D":
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "NE":
            self.position = (self.position[0] + 1, self.position[1] + 1)
        elif direction == "SE":
            self.position = (self.position[0] + 1, self.position[1] - 1)
        elif direction == "SW":
            self.position = (self.position[0] - 1, self.position[1] - 1)
        elif direction == "NW":
            self.position = (self.position[0] - 1, self.position[1] + 1)
        else:
            print(direction)
            raise ValueError(f" {direction} is invalid direction ")

    def move(self, instruction):
        print(f"moving in base class {self.name}")
        direction, distance = self.process_instruction(instruction)
        for _ in range(0, distance):
            self._step(direction)

    def step(self, direction):
        print(f"stepping in {self.name}")
        if direction is not None:
            self._step(direction)
        self.position_history.append(self.position)


class Tail(Knot):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.tailknot = True


class Head(Knot):
    def __init__(self, name, position, tail):
        super().__init__(name, position)
        self.tail = tail

    def determine_tail_move(self):
        x_diff = self.position[0] - self.tail.position[0]
        y_diff = self.position[1] - self.tail.position[1]
        if np.abs(x_diff) > 2 or np.abs(y_diff) > 2:
            # self.draw((10, 10))
            raise ValueError(" oh dear something is wrong ")
        # diagonal up and right
        elif (
            (x_diff == 2 and y_diff == 1)
            or (x_diff == 1 and y_diff == 2)
            or (x_diff == 2 and y_diff == 2)
        ):
            return "NE"
        # diagonal down and right
        elif (
            (x_diff == 2 and y_diff == -1)
            or (x_diff == 1 and y_diff == -2)
            or (x_diff == 2 and y_diff == -2)
        ):
            return "SE"
        # diagonal down and left
        elif (
            (x_diff == -2 and y_diff == -1)
            or (x_diff == -1 and y_diff == -2)
            or (x_diff == -2 and y_diff == -2)
        ):
            return "SW"
        # diagonal up and left
        elif (
            (x_diff == -2 and y_diff == 1)
            or (x_diff == -1 and y_diff == 2)
            or (x_diff == -2 and y_diff == 2)
        ):
            return "NW"
        # left
        elif x_diff == -2 and y_diff == 0:
            return "L"
        # right
        elif x_diff == 2 and y_diff == 0:
            return "R"
        # down
        elif x_diff == 0 and y_diff == -2:
            return "D"
        # up
        elif x_diff == 0 and y_diff == 2:
            return "U"

    def step(self, direction):
        super().step(direction)
        tail_dir = self.determine_tail_move()
        self.tail.step(tail_dir)

    def move(self, instruction):
        # move head,
        # move tail
        # move tails tail
        print(f"moving in {self.name}")
        direction, distance = super().process_instruction(instruction)
        for _ in range(0, distance):
            self.step(direction)

            # self.draw()

    def draw(self, size=(5, 5)):
        grid = np.empty(size, dtype="str")
        grid[:] = "."

        def coords_to_array_index(coords, size):
            x_index = size[0] - 1 - coords[1]
            y_index = coords[0]
            return x_index, y_index

        head_i, head_j = coords_to_array_index(self.position, size)
        grid[head_i, head_j] = "H"
        tail_i, tail_j = coords_to_array_index(self.tail.position, size)
        grid[tail_i, tail_j] = "T"

        pprint(grid)


if __name__ == "__main__":

    with open("/Users/TimothyW/Fun/avent_of_code/2022/day_nine/input.txt", "r") as f:
        lines = f.readlines()

    # tail = Tail("tail", (0, 0))
    # head = Head("head", (0, 0), tail)

    # for line in lines:
    #     head.move(line.strip("\n"))

    print("hello world")
    last_knot = None
    for i in range(0, 10):
        if i == 0:
            label_n = 9 - i
            tail = Tail(f"{label_n}", (0, 0))
            last_knot = tail
        else:
            label_n = 9 - i
            head = Head(f"{label_n}", (0, 0), last_knot)
            last_knot = head

    p2_head = last_knot
    for line in lines:
        p2_head.move(line.strip("\n"))

    print("hello world")
