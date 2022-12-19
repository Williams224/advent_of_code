import numpy as np
from itertools import cycle
import uuid
from datetime import datetime
import pandas as pd

# generate object which is a shape and coordinate of lowest and most left point
# step:
# push left or right
# push down

# world map with size 7 *10k
# all coords in world frame.


class Shape:
    n_shapes_on_map = 0

    def __init__(self, coord):
        self.coord = coord
        self.points_occupied = []
        self.id = uuid.uuid4()

    def add_to_map(self, wmap, finished):
        if finished:
            val = 1
        else:
            val = 2
        for p in self.points_occupied:
            wmap[p[1], p[0]] = val

        self.n_shapes_on_map += 1

        return wmap

    def __str__(self) -> str:
        a = np.zeros((10000, 7))
        for p in self.points_occupied:
            a[p[1], p[0]] = 2

        return np.array2string(a[9989:10000, :])

    def _get_right_most_point(self):
        return self.points_occupied.sort(key=lambda t: t[0], reverse=True)[0]

    def process_jet_inst(self, inst, wmap):
        move_possible = True
        if inst == ">":
            for p in self.points_occupied:
                new_point = (p[0] + 1, p[1])
                if new_point[0] > 6:
                    move_possible = False
                    continue
                if wmap[new_point[1], new_point[0]] != 0 and move_possible:
                    move_possible = False

            if move_possible:
                for i in range(0, len(self.points_occupied)):
                    self.points_occupied[i] = (
                        self.points_occupied[i][0] + 1,
                        self.points_occupied[i][1],
                    )
        move_possible = True
        if inst == "<":
            for p in self.points_occupied:
                new_point = (p[0] - 1, p[1])
                if new_point[0] < 0:
                    move_possible = False
                if wmap[new_point[1], new_point[0]] != 0 and move_possible:
                    move_possible = False

            if move_possible:
                for i in range(0, len(self.points_occupied)):
                    self.points_occupied[i] = (
                        self.points_occupied[i][0] - 1,
                        self.points_occupied[i][1],
                    )

    def move_down(self, wmap):
        for p in self.points_occupied:
            new_point = (p[0], p[1] + 1)
            if new_point[1] > (wmap.shape[0] - 1):
                return True
            if wmap[new_point[1], new_point[0]] != 0:
                return True

        for i in range(0, len(self.points_occupied)):
            self.points_occupied[i] = (
                self.points_occupied[i][0],
                self.points_occupied[i][1] + 1,
            )

        return False


class Square(Shape):
    def __init__(self, coord):
        super().__init__(coord)
        # work in x, y
        self.points_occupied = [
            (self.coord[0], self.coord[1]),
            (self.coord[0] + 1, self.coord[1]),
            (self.coord[0], self.coord[1] - 1),
            (self.coord[0] + 1, self.coord[1] - 1),
        ]


class VertLine(Shape):
    def __init__(self, coord):
        super().__init__(coord)
        self.points_occupied = [
            (self.coord[0], self.coord[1]),
            (self.coord[0], self.coord[1] - 1),
            (self.coord[0], self.coord[1] - 2),
            (self.coord[0], self.coord[1] - 3),
        ]


class LShape(Shape):
    def __init__(self, coord):
        super().__init__(coord)
        self.points_occupied = [
            (self.coord[0], self.coord[1]),
            (self.coord[0] + 1, self.coord[1]),
            (self.coord[0] + 2, self.coord[1]),
            (self.coord[0] + 2, self.coord[1] - 1),
            (self.coord[0] + 2, self.coord[1] - 2),
        ]


class Cross(Shape):
    def __init__(self, coord):
        super().__init__((coord[0] + 1, coord[1]))
        self.points_occupied = [
            (self.coord[0], self.coord[1]),
            (self.coord[0], self.coord[1] - 1),
            (self.coord[0], self.coord[1] - 2),
            (self.coord[0] - 1, self.coord[1] - 1),
            (self.coord[0] + 1, self.coord[1] - 1),
        ]


class HLine(Shape):
    def __init__(self, coord):
        super().__init__(coord)
        self.points_occupied = [
            (self.coord[0], self.coord[1]),
            (self.coord[0] + 1, self.coord[1]),
            (self.coord[0] + 2, self.coord[1]),
            (self.coord[0] + 3, self.coord[1]),
        ]

        # print("h")


def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    return list(lines[0])


def draw_world_map(wmap, n_rows=10):
    l = 100000 - n_rows
    a = wmap[l:100000, :]
    print(np.array2string(a))


def get_height(wmap):
    max_height = np.where(wmap != 0)[0].min()
    return 99999 - max_height + 1


if __name__ == "__main__":

    input = read_input("/Users/TimothyW/Fun/avent_of_code/2022/day_seventeen/input.txt")

    instructions = cycle(input)

    world_map = np.zeros((100000, 7))

    shapes = cycle([HLine, Cross, LShape, VertLine, Square])

    data = []
    start = datetime.now()
    for rock in range(0, 25000):

        shape_init = next(shapes)
        if rock == 0:
            shape = shape_init((2, 99999 - 3))
        else:
            current_hightest = np.where(world_map != 0)[0].min()
            shape = shape_init((2, current_hightest - 4))

        # print(shape)
        finished = False
        while not finished:
            temp_map = world_map
            jet_inst = next(instructions)
            # print(jet_inst)
            shape.process_jet_inst(jet_inst, world_map)
            # print(shape)
            finished = shape.move_down(world_map)
            # print(shape)
            if finished:
                shape.add_to_map(world_map, finished)

        height = get_height(world_map)
        data.append({"rock_i": rock, "height": height})
        # if rock % 40 == 0:
        # print(f"Rock N, {rock} , {height}")
    end = datetime.now()

    time_taken = (end - start).seconds
    print(time_taken)
    df = pd.DataFrame(data)
    df.to_csv("real_data.csv", header=True)
