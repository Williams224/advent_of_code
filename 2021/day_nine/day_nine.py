from os import X_OK
import numpy as np
from numpy.core.defchararray import find
from numpy.lib.twodim_base import _min_int


def test_element_local_minima(x, y, arr):
    val = arr[y][x]
    if y > 0:
        left_neighbour = arr[y - 1][x]
        if left_neighbour <= val:
            return False
    if x > 0:
        top_neighbour = arr[y][x - 1]
        if top_neighbour <= val:
            return False
    if x < 99:
        bottom_neighbour = arr[y][x + 1]
        if bottom_neighbour <= val:
            return False
    if y < 99:
        right_neighbour = arr[y + 1][x]
        if right_neighbour <= val:
            return False

    return True


def find_basin_value(minima_x, minima_y, arr, direction, coords_same_basin):
    # consider go right first
    max_x = arr.shape[1] - 1
    max_y = arr.shape[0] - 1
    minima_val = arr[minima_y][minima_x]
    if direction == "right":
        if minima_x < max_x:
            right_value = arr[minima_y][minima_x + 1]
            if right_value > minima_val and right_value < 9:
                print("found right")
                coords_same_basin.append((minima_x + 1, minima_y))
                return find_basin_value(
                    minima_x + 1, minima_y, arr, direction, coords_same_basin
                )
    # go left
    elif direction == "left":
        if minima_x > 0:
            left_value = arr[minima_y][minima_x - 1]
            if left_value > minima_val and left_value < 9:
                print("found left")
                coords_same_basin.append((minima_x - 1, minima_y))
                return find_basin_value(
                    minima_x - 1, minima_y, arr, direction, coords_same_basin
                )
    elif direction == "down":
        if minima_y < max_y:
            below_value = arr[minima_y + 1][minima_x]
            if below_value > minima_val and below_value < 9:
                print("found down")
                coords_same_basin.append((minima_x, minima_y + 1))
                return find_basin_value(
                    minima_x, minima_y + 1, arr, direction, coords_same_basin
                )
    elif direction == "up":
        if minima_y > 0:
            up_value = arr[minima_y - 1][minima_x]
            if up_value > minima_val and up_value < 9:
                print("found up")
                coords_same_basin.append((minima_x, minima_y - 1))
                return find_basin_value(
                    minima_x, minima_y - 1, arr, direction, coords_same_basin
                )

    else:
        print("WRONG DIRECTIOn")
        return None

    return coords_same_basin


def read_input_map(path):
    with open(path, "r") as f:
        lines = f.readlines()
    lines_lists = []
    for l in lines:
        lines_lists.append(list(l.strip("\n")))

    map = np.array(lines_lists, dtype=int)
    return map


def find_draining_basin(x, y, arr, id_matrix):
    max_x = arr.shape[1] - 1
    max_y = arr.shape[0] - 1
    minima_val = arr[y][x]
    if x < max_x:
        right_value = arr[y][x + 1]
        if right_value < minima_val and right_value > 0:
            draining_id = id_matrix[y][x + 1]
            id_matrix[y][x] = draining_id
            return id_matrix
    if x > 0:
        left_value = arr[y][x - 1]
        if left_value < minima_val and left_value > 0:
            draining_id = id_matrix[y][x - 1]
            id_matrix[y][x] = draining_id
            return id_matrix

    if y < max_y:
        below_value = arr[y + 1][x]
        if below_value < minima_val and below_value > 0:
            draining_id = id_matrix[y + 1][x]
            id_matrix[y][x] = draining_id
            return id_matrix

    if y > 0:
        up_value = arr[y - 1][x]
        if up_value < minima_val and up_value > 0:
            draining_id = id_matrix[y - 1][x]
            id_matrix[y][x] = draining_id
            return id_matrix

    return id_matrix


if __name__ == "__main__":

    map = read_input_map("day_nine/input.txt")

    minima_vals = []
    for x in range(0, 100):
        for y in range(0, 100):
            if test_element_local_minima(x, y, map):
                minima_vals.append(map[x][y])

    print(np.sum(np.array(minima_vals) + 1))

    # Part 2
    # define grid of indicators -1 = unmarked, 0 = minima, 1+ = identifier 9 = 9
    # start with lowest value and check if minima + mark
    # recursively search each way from minima and mark with same ID, ignoring values already marked + remove from list to be checked
    #

    id_matrix = np.zeros((100, 100)) - 1

    test_map = read_input_map("day_nine/input.txt")

    priority_list = set(np.sort(test_map.flatten()))

    y_minima, x_minima = np.where(test_map == 9)
    for nx, ny in zip(x_minima, y_minima):
        id_matrix[ny][nx] = 9

    basin_id = 10
    for t in range(0, 9):
        y_minima, x_minima = np.where(test_map == t)
        for x, y in zip(x_minima, y_minima):
            if test_element_local_minima(x, y, test_map):
                id_matrix[y][x] = basin_id
                same_coords = find_basin_value(x, y, test_map, "left", [])
                same_coords = find_basin_value(x, y, test_map, "right", same_coords)
                same_coords = find_basin_value(x, y, test_map, "up", same_coords)
                same_coords = find_basin_value(x, y, test_map, "down", same_coords)
                print(same_coords)
                for sx, sy in same_coords:
                    id_matrix[sy][sx] = basin_id
                basin_id += 1
    attempt_n = 1
    while np.any(id_matrix == -1):
        for x in range(0, 100):
            for y in range(0, 100):
                if id_matrix[y][x] == -1:
                    id_matrix = find_draining_basin(x, y, test_map, id_matrix)
        print(f"attempts {attempt_n}")
        attempt_n += 1

    vals, counts = np.unique(id_matrix[id_matrix != 9], return_counts=True)
    counts = np.sort(counts)

    print(counts[-1] * counts[-2] * counts[-3])
    print("h")