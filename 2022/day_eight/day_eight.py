import numpy as np


def load_data(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]

    map = np.array([[int(line[i]) for i in range(0, len(line))] for line in lines])

    return map


def calc_diff_coords(init, now):
    i_move = np.abs(init[0] - now[0])
    j_move = np.abs(init[1] - now[1])
    if j_move != 0 and i_move != 0:
        raise ValueError
    return max(i_move, j_move)


def check_less_than(i, j, val, map, stage):
    if i < 0:
        return True, (0, j)
    if j < 0:
        return True, (i, 0)
    if i > map.shape[0] - 1:
        return True, (map.shape[0] - 1, j)
    if j > map.shape[1] - 1:
        return True, (i, map.shape[1] - 1)

    if stage == "initial":
        up_vis_b, up_coords = check_less_than(i - 1, j, val, map, "up")
        down_vis_b, down_coords = check_less_than(i + 1, j, val, map, "down")
        left_vis_b, left_coords = check_less_than(i, j - 1, val, map, "left")
        right_vis_b, right_coords = check_less_than(i, j + 1, val, map, "right")
        left_vis = calc_diff_coords((i, j), left_coords)
        right_vis = calc_diff_coords((i, j), right_coords)
        up_vis = calc_diff_coords((i, j), up_coords)
        down_vis = calc_diff_coords((i, j), down_coords)
        return left_vis_b or right_vis_b or up_vis_b or down_vis_b, (
            left_vis,
            right_vis,
            up_vis,
            down_vis,
        )
    elif map[i, j] >= val:
        return False, (i, j)
    elif stage == "left":
        return check_less_than(i, j - 1, val, map, "left")
    elif stage == "right":
        return check_less_than(i, j + 1, val, map, "right")
    elif stage == "up":
        return check_less_than(i - 1, j, val, map, "up")
    elif stage == "down":
        return check_less_than(i + 1, j, val, map, "down")


def count_visible(map):
    total = 0
    for i in range(1, map.shape[0] - 1):
        for j in range(1, map.shape[1] - 1):
            if check_less_than(i, j, map[i, j], map, "initial")[0]:
                total = total + 1

    return total


def calc_external_visible(map):
    return (map.shape[0] * 2) + ((map.shape[1] - 2) * 2)


def calc_scenic_scores(map):
    scores = []
    for i in range(1, map.shape[0] - 1):
        scores_row = []
        for j in range(1, map.shape[1] - 1):
            _, vises = check_less_than(i, j, map[i, j], map, "initial")
            scenic_score = vises[0] * vises[1] * vises[2] * vises[3]
            scores_row.append(scenic_score)
        scores.append(scores_row)

    return scores


if __name__ == "__main__":

    map = load_data("/Users/TimothyW/Fun/avent_of_code/2022/day_eight/input.txt")

    interior_visible = count_visible(map)

    external_visible = calc_external_visible(map)
    print(interior_visible)

    total_visible = interior_visible + external_visible

    print(total_visible)

    scenic_scores = calc_scenic_scores(map)

    print("hello worlds")
