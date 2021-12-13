from os import X_OK, path
import numpy as np
from tabulate import tabulate


def fold(val, axis, coord):
    if axis == "y":
        if coord[1] > val:
            new_x = coord[0]
            new_y = 2 * val - coord[1]
        else:
            new_x = coord[0]
            new_y = coord[1]
    elif axis == "x":
        if coord[0] > val:
            new_y = coord[1]
            new_x = 2 * val - coord[0]
        else:
            new_x = coord[0]
            new_y = coord[1]

    return new_x, new_y


if __name__ == "__main__":
    with open("day_thirteen/input.txt") as f:
        lines = f.readlines()

    map = np.zeros((6, 40))

    coords = []
    for line in lines:
        coord = np.array(line.strip("\n").split(","), dtype=int)
        coords.append(coord)
        folded_x, folded_y = fold(
            6,
            "y",
            fold(
                13,
                "y",
                fold(
                    27,
                    "y",
                    fold(
                        40,
                        "x",
                        fold(
                            55,
                            "y",
                            fold(
                                81,
                                "x",
                                fold(
                                    111,
                                    "y",
                                    fold(
                                        163,
                                        "x",
                                        fold(
                                            223,
                                            "y",
                                            fold(
                                                327,
                                                "x",
                                                fold(447, "y", fold(655, "x", coord)),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        )
        map[folded_y][folded_x] += 1
    string_map = map.astype(str)
    string_map[map >= 1] = "#"
    string_map[map == 0] = "."
    print(tabulate(string_map))

    # print(np.sum(map > 0))
