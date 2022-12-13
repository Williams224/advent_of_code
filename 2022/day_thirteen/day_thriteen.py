import json
import numpy as np


def check_list(left_list, right_list, i):
    if left_list == [[2]] or right_list == [[2]]:
        print("H")
    left_list_ran_out = i > (len(left_list) - 1)
    right_list_ran_out = i > (len(right_list) - 1)

    if left_list_ran_out and not right_list_ran_out:
        return True
    if right_list_ran_out and not left_list_ran_out:
        return False

    if left_list_ran_out and right_list_ran_out:
        return None

    if type(left_list[i]) == list or type(right_list[i]) == list:  # true for [[2]]
        new_left_list = left_list.copy()
        new_right_list = right_list.copy()
        if type(left_list[i]) == int:
            new_left_list[i] = [left_list[i]]
        elif type(right_list[i]) == int:
            new_right_list[i] = [right_list[i]]
        inner_check = check_list(new_left_list[i], new_right_list[i], 0)
        if inner_check == True or inner_check == False:
            return inner_check
        else:
            pass
            # print("#")

    else:
        # print(left_list[i], right_list[i])
        if left_list[i] < right_list[i]:
            return True
        elif left_list[i] > right_list[i]:
            return False

    return check_list(left_list, right_list, i + 1)


def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
    lines = [line.strip("\n") for line in lines]
    lines_iter = iter(lines)
    pairs = []
    while True:
        left = next(lines_iter)
        right = next(lines_iter)
        pairs.append((json.loads(left), json.loads(right)))
        if next(lines_iter, None) == None:
            break

    return pairs


def read_input_p2(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]
    flat_lines = []
    for line in lines:
        if line == "":
            continue
        flat_lines.append(json.loads(line))

    return flat_lines


def bubble_sort(input_list):
    n = len(input_list)
    swaps = True
    iters = 0
    while swaps:
        swaps = False

        for i in range(0, n - 1):
            if i == 299:
                print(input_list[i])
                print("bef")
            if not check_list(input_list[i], input_list[i + 1], 0):  # [[2]]
                if i == 300:
                    print("ha")
                temp = input_list[i + 1]
                input_list[i + 1] = input_list[i]
                input_list[i] = temp
                swaps = True
        iters += 1
    return input_list


if __name__ == "__main__":

    pairs = read_input("/Users/TimothyW/Fun/avent_of_code/2022/day_thirteen/input.txt")
    outcomes = []
    for pair in pairs:
        outcomes.append(check_list(pair[0], pair[1], 0))

    indices_sum = np.sum((np.where(np.array(outcomes))[0] + 1))

    print(f"indices sum = {indices_sum}")

    flat_input = read_input_p2(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_thirteen/input.txt"
    )

    flat_input.append([[2]])
    flat_input.append([[6]])

    sorted_input = bubble_sort(flat_input)

    print("h")
