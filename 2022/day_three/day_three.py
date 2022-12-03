import numpy as np


def get_char_priority(char):
    if char.islower():
        return ord(char) - ord("a") + 1

    return ord(char) - ord("A") + 27


def line_priority_score(line):
    split_index = int(len(line) / 2.0)
    comp_one = set(line[:split_index])
    comp_two = set(line[split_index:])

    common_char = list(comp_two.intersection(comp_one))[0]

    return get_char_priority(common_char)


def get_group(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def get_group_priority_score(gr_list):
    assert len(gr_list) == 3
    common_char = (
        set(gr_list[0]).intersection(set(gr_list[1])).intersection(set(gr_list[2]))
    )
    return get_char_priority(list(common_char)[0])


if __name__ == "__main__":
    with open("/Users/TimothyW/Fun/avent_of_code/2022/day_three/input.txt", "r") as f:
        lines = f.readlines()

    lines = list(map(lambda x: x.strip("\n"), lines))

    scores = list(map(line_priority_score, lines))
    print(np.sum(scores))

    groups = [gr for gr in get_group(lines, 3)]
    group_scores = list(map(get_group_priority_score, groups))
    print(np.sum(group_scores))
