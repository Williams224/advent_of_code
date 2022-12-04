import numpy as np


def section_to_tuple(section_str):
    split_section_str = section_str.strip("\n").split("-")
    return (int(split_section_str[0]), int(split_section_str[1]))


def line_to_sections(line):
    sections = line.split(",")
    return (section_to_tuple(sections[0]), section_to_tuple(sections[1]))


def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    sections = list(map(line_to_sections, lines))
    return sections


def separate_big_small(sections_pair):
    first_section_length = sections_pair[0][1] - sections_pair[0][0]
    second_section_length = sections_pair[1][1] - sections_pair[1][0]

    if second_section_length > first_section_length:
        bigsection = sections_pair[1]
        smallsection = sections_pair[0]
    else:
        bigsection = sections_pair[0]
        smallsection = sections_pair[1]

    return bigsection, smallsection


def check_full_overlap(sections_pair):
    bigsection, smallsection = separate_big_small(sections_pair)

    return smallsection[0] >= bigsection[0] and smallsection[1] <= bigsection[1]


def check_any_overlap(sections_pair):
    bigsection, smallsection = separate_big_small(sections_pair)

    if smallsection[0] >= bigsection[0] and smallsection[0] <= bigsection[1]:
        return True

    if smallsection[1] >= bigsection[0] and smallsection[1] <= bigsection[1]:
        return True

    return False


if __name__ == "__main__":

    sections = read_input("/Users/TimothyW/Fun/avent_of_code/2022/day_four/input.txt")

    total_overlaps = np.sum(list(map(check_full_overlap, sections)))
    print(total_overlaps)

    partial_overlaps = np.sum(list(map(check_any_overlap, sections)))
    print(partial_overlaps)
