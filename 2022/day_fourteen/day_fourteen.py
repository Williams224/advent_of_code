import numpy as np


class Cave:
    def __init__(self, rocks_list):
        self.x_min = 999999
        self.y_min = 999999
        self.x_max = 0
        self.y_max = 0
        self.total_sands = 0
        for rock in rocks_list:
            for vertex in rock:
                if vertex[0] < self.x_min:
                    self.x_min = vertex[0]
                if vertex[0] > self.x_max:
                    self.x_max = vertex[0]
                if vertex[1] < self.y_min:
                    self.y_min = vertex[1]
                if vertex[1] > self.y_max:
                    self.y_max = vertex[1]
        self.ext = 300
        self.x_range = self.x_max - self.x_min + 1
        self.world_map = np.zeros((self.y_max + 3, self.x_range + self.ext))

        print(self.world_map)

    # 500 -> half way across -> 15
    def to_world_coords(self, coord):
        total_range = self.x_range + self.ext
        half_way = int(total_range / 2)
        transformation = 500 - half_way
        return (coord[1], coord[0] - transformation)

    def add_rocks(self, start, end):
        start_world_c = self.to_world_coords(start)
        end_world_c = self.to_world_coords(end)
        # vertical or horizontal:
        if start_world_c[0] != end_world_c[0]:
            axis = 0
        else:
            axis = 1

        for i in range(
            min(start_world_c[axis], end_world_c[axis]),
            max(start_world_c[axis], end_world_c[axis]) + 1,
        ):
            if axis == 0:
                self.world_map[i, start_world_c[1]] = 1
            else:
                self.world_map[start_world_c[0], i] = 1

        print("hafa")

    def take_sand_step(self, sand_coord):
        if sand_coord[1] >= self.world_map.shape[1] - 1:
            print(" need to make world map bigger")
            print("insufficient shape is ", self.world_map.shape)
            raise ValueError

        if self.world_map[sand_coord[0] + 1, sand_coord[1]] == 0:
            return (sand_coord[0] + 1, sand_coord[1]), True
        elif self.world_map[sand_coord[0] + 1, sand_coord[1] - 1] == 0:
            return (sand_coord[0] + 1, sand_coord[1] - 1), True
        elif self.world_map[sand_coord[0] + 1, sand_coord[1] + 1] == 0:
            return (sand_coord[0] + 1, sand_coord[1] + 1), True
        else:
            return sand_coord, False

    def add_sand(self, start_point):
        sand_coord = self.to_world_coords(start_point)
        con = True
        while con:
            sand_coord, con = self.take_sand_step(sand_coord)

        self.total_sands += 1
        self.world_map[sand_coord[0], sand_coord[1]] = 2
        if sand_coord[0] == 0:
            return False

        return True

    def add_floor(self):
        for i in range(0, self.world_map.shape[1]):
            y_max = self.world_map.shape[0] - 1
            self.world_map[y_max, i] = 1


# world
# init
# drop sand
def read_rocks_list(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]
    rocks_list = []
    for line in lines:
        coords = line.split("->")
        coords = [
            (int(coord.split(",")[0]), int(coord.split(",")[1])) for coord in coords
        ]
        rocks_list.append(coords)
    return rocks_list


if __name__ == "__main__":

    rocks_list = read_rocks_list(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_fourteen/input.txt"
    )
    cave = Cave(rocks_list)

    for rock in rocks_list:
        for i in range(0, len(rock) - 1):
            cave.add_rocks(rock[i], rock[i + 1])

    cave.add_floor()
    add_more_sand = True
    while add_more_sand:
        add_more_sand = cave.add_sand((500, 0))
        print(cave.world_map)

    print(cave.total_sands)
    print("hashdhasd")
