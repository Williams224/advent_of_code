import numpy as np


def initialize_state_dict(start_list, pair_counts):

    for i in range(0, len(start_list) - 1):
        pair = start_list[i] + start_list[i + 1]
        pair_counts[pair] += 1

    return pair_counts


def make_step(pair_counts, inserts):
    new_pair_counts = pair_counts.copy()
    for pair, count in pair_counts.items():
        if count > 0:
            insert_char = inserts[pair]
            new_pair_one = pair[0] + insert_char
            new_pair_two = insert_char + pair[1]
            new_pair_counts[new_pair_one] += count
            new_pair_counts[new_pair_two] += count
            new_pair_counts[pair] -= count

    return new_pair_counts


if __name__ == "__main__":
    with open("day_fourteen/input.txt") as f:
        lines = f.readlines()

    starting = list("SVCHKVFKCSHVFNBKKPOC")
    insertions = {}
    pair_counts = {}
    for line in lines:
        insertion = line.strip("\n").split(" -> ")
        insertions[insertion[0]] = insertion[1]
        pair_counts[insertion[0]] = 0

    pair_counts = initialize_state_dict(starting, pair_counts)

    polymer = starting
    print(pair_counts)
    for i in range(0, 40):
        pair_counts = make_step(pair_counts, insertions)

    print(pair_counts)

    unique_elements = np.unique(starting)
    element_counts = {u: 0 for u in unique_elements}
    for p, c in pair_counts.items():
        element_counts[p[0]] += c

    element_counts[starting[-1]] += 1

    print(element_counts)
    print(np.max(list(element_counts.values())) - np.min(list(element_counts.values())))