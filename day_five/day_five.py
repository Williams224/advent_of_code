import numpy as np


def values_between_vals(a, b):
    if a > b:
        return list(range(a, b - 1, -1))
    elif a < b:
        return list(range(a, b + 1))
    return []


def line_to_coordinates(line):
    coords_pair = line.rstrip("\n").split(" -> ")
    ret_cords = []
    for coords in coords_pair:
        ret_cords.append(tuple([int(c) for c in coords.split(",")]))

    return tuple(ret_cords)


class World:
    def __init__(self, x_size, y_size):
        self.world_map = np.zeros((x_size, y_size), dtype=int)

    def add_line(self, coordinates):
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        # vertical
        if x1 == x2:
            v_range = [y1, y2]
            v_range.sort()
            for y in range(v_range[0], v_range[1] + 1):
                self.world_map[x1][y] += 1
        # horizontal
        elif y1 == y2:
            h_range = [x1, x2]
            h_range.sort()
            for x in range(h_range[0], h_range[1] + 1):
                self.world_map[x][y1] += 1
        # diagonal
        else:
            x_vals = values_between_vals(x1, x2)
            y_vals = values_between_vals(y1, y2)
            for x, y in zip(x_vals, y_vals):
                self.world_map[x][y] += 1

    def get_n_great_n(self, n):
        return np.sum(self.world_map >= n)


if __name__ == "__main__":
    with open("day_five/input.txt") as f:
        lines = f.readlines()

    line_list = [line_to_coordinates(line) for line in lines]
    only_straight_lines = list(
        filter(lambda t: (t[0][0] == t[1][0]) or (t[0][1] == t[1][1]), line_list)
    )

    W = World(1000, 1000)

    for osl in only_straight_lines:
        W.add_line(osl)

    print(W.get_n_great_n(2))

    W_all = World(1000, 1000)

    for line in line_list:
        W_all.add_line(line)

    print(W_all.get_n_great_n(2))
