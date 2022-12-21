import numpy as np
from itertools import cycle
import math
import json


def load_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines = [int(line.strip("\n")) for line in lines]

    return lines


def get_new_index(old_index, val, N):
    diff = old_index + val
    new_index = diff % (N - 1)
    return new_index


OPERATIONS = []


def move_element(orig_list, i, new_list):
    if i == 293:
        print("break now")

    N = len(orig_list)
    val = orig_list[i][1]
    old_index = new_list.index(orig_list[i])
    new_index = get_new_index(old_index, val, N)
    new_list.insert(new_index, new_list.pop(old_index))
    # print(f" moved {val} from {old_index} to {new_index}")
    # OPERATIONS.append(f" moved {val} from {old_index} to {new_index}")
    return new_list


if __name__ == "__main__":

    multiplier = 811589153
    vals = load_input("/Users/TimothyW/Fun/avent_of_code/2022/day_twenty/input.txt")
    vals_indexed = [(i, vals[i] * multiplier) for i in range(0, len(vals))]

    N = len(vals_indexed)
    orig_list = vals_indexed.copy()
    new_list = vals_indexed.copy()
    for _ in range(0, 10):
        for i in range(0, N):
            new_list = move_element(orig_list, i, new_list)
        # print(f"Move {val} from {old_index} to {new_index}")
        # print(new_list)

    output_vals = list(map(lambda x: x[1], new_list))
    mixed = np.array(output_vals)
    # np.save(open("mineout.txt", "wb"), mixed)
    zero_index = np.where(mixed == 0)[0][0]
    thousand = mixed[(1000 + zero_index) % len(mixed)]
    two_thousand = mixed[(2000 + zero_index) % len(mixed)]
    three_thousand = mixed[(3000 + zero_index) % len(mixed)]
    print(thousand + two_thousand + three_thousand)

    # with open("mineoperations.txt", "w") as f:
    # json.dump(OPERATIONS, f)
    """ counter = 0
    cyclic_iterator = cycle(new_list)
    zero_found = False
    grove_vals = []
    while counter < 3001:
        val = next(cyclic_iterator)
        if counter == 1000 or counter == 2000 or counter == 3000:
            print(counter, val)
            grove_vals.append(val)
        if val == 0 and not zero_found:
            zero_found = True
        if zero_found:
            counter += 1 """

    # print(np.sum(grove_vals))
