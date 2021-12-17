import numpy as np
from datetime import date, datetime


def cost_of_path(path, map):
    total_cost = 0
    for coords in path:
        total_cost += map[coords[0]][coords[1]]

    return total_cost


def find_all_paths(start_node, end_node, path=[]):
    path = path + [start_node]
    if start_node == end_node:
        return [path]
    paths = []
    down_coords = (start_node[0] + 1, start_node[1])
    right_coords = (start_node[0], start_node[1] + 1)
    if down_coords[0] <= end_node[0] and down_coords not in path:
        down_paths = find_all_paths(down_coords, end_node, path)
        for dp in down_paths:
            paths.append(dp)
    if right_coords[1] <= end_node[1] and right_coords not in path:
        right_paths = find_all_paths(right_coords, end_node, path)
        for rp in right_paths:
            paths.append(rp)
    return paths


if __name__ == "__main__":

    with open("day_fifteen/input.txt", "r") as f:
        lines = f.readlines()

    lines = [list(l.strip("\n")) for l in lines]

    cost_map = np.array(lines, dtype=int)

    start = datetime.now()
    all_paths = find_all_paths((0, 0), (19, 19), [])
    end = datetime.now()

    print((end - start).seconds)

    costs = list(map(lambda x: cost_of_path(x, cost_map), all_paths))
    print(np.min(costs) - 1)
