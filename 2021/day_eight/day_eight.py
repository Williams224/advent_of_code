import numpy as np

SEGMENTS_TO_DIGITS = {
    "ABCEFG": 0,
    "CF": 1,
    "ACDEG": 2,
    "ACDFG": 3,
    "BCDF": 4,
    "ABDFG": 5,
    "ABDEFG": 6,
    "ACF": 7,
    "ABCDEFG": 8,
    "ABCDFG": 9,
}


def find_with_n_chars(wires_list, n_chars):
    found = list(filter(lambda x: len(x) == n_chars, wires_list))
    if len(found) == 1:
        return found[0]
    return found


def determine_segment_A(seven_signal, one_signal):
    for char in seven_signal:
        if char not in one_signal:
            return char

    return None


def determine_segment_E(wires_list):
    two_chars = find_with_n_chars(wires_list, 2)
    four_chars = find_with_n_chars(wires_list, 4)
    three_chars = find_with_n_chars(wires_list, 3)
    six_chars = find_with_n_chars(wires_list, 6)
    seven_chars = find_with_n_chars(wires_list, 7)
    candidates = []
    for c in seven_chars:
        if c not in three_chars and c not in four_chars and c not in two_chars:
            candidates.append(c)

    for c in candidates:
        in_sixes = list(map(lambda x: c in x, six_chars))
        if np.sum(np.array(in_sixes)) == 2:
            return c

    return None


def determine_segment_D(wires_list):
    two_chars = find_with_n_chars(wires_list, 2)
    four_chars = find_with_n_chars(wires_list, 4)
    six_chars = find_with_n_chars(wires_list, 6)
    for option in six_chars:
        for c in four_chars:
            if c not in two_chars and c not in option:
                return c
    return None


def count_n_in(char, list_seqs):
    in_seqs = list(map(lambda x: char in x, list_seqs))
    return np.sum(np.array(in_seqs))


def determine_segment_C(wires_list):
    two_chars = find_with_n_chars(wires_list, 2)
    three_chars = find_with_n_chars(wires_list, 3)
    four_chars = find_with_n_chars(wires_list, 4)
    five_chars = find_with_n_chars(wires_list, 5)
    six_chars = find_with_n_chars(wires_list, 6)
    seven_chars = find_with_n_chars(wires_list, 7)
    for c in seven_chars:
        if c not in three_chars:
            continue
        if c not in four_chars:
            continue
        if c not in two_chars:
            continue
        if count_n_in(c, six_chars) == 2 and count_n_in(c, five_chars) == 2:
            return c

    return None


def determine_segment_B(wires_list):
    two_chars = find_with_n_chars(wires_list, 2)
    three_chars = find_with_n_chars(wires_list, 3)
    four_chars = find_with_n_chars(wires_list, 4)
    five_chars = find_with_n_chars(wires_list, 5)
    six_chars = find_with_n_chars(wires_list, 6)
    seven_chars = find_with_n_chars(wires_list, 7)
    for c in seven_chars:
        if c in two_chars:
            continue
        if c in three_chars:
            continue
        if c not in four_chars:
            continue
        if count_n_in(c, five_chars) == 1 and count_n_in(c, six_chars) == 3:
            return c

    return None


def determine_segment_F(wires_list):
    two_chars = find_with_n_chars(wires_list, 2)
    three_chars = find_with_n_chars(wires_list, 3)
    four_chars = find_with_n_chars(wires_list, 4)
    five_chars = find_with_n_chars(wires_list, 5)
    six_chars = find_with_n_chars(wires_list, 6)
    seven_chars = find_with_n_chars(wires_list, 7)
    for c in seven_chars:
        if c not in two_chars:
            continue
        if c not in three_chars:
            continue
        if c not in four_chars:
            continue
        if count_n_in(c, five_chars) == 2 and count_n_in(c, six_chars) == 3:
            return c

    return None


def determine_segment_G(wires_list):
    two_chars = find_with_n_chars(wires_list, 2)
    three_chars = find_with_n_chars(wires_list, 3)
    four_chars = find_with_n_chars(wires_list, 4)
    five_chars = find_with_n_chars(wires_list, 5)
    six_chars = find_with_n_chars(wires_list, 6)
    seven_chars = find_with_n_chars(wires_list, 7)
    for c in seven_chars:
        if c in two_chars:
            continue
        if c in three_chars:
            continue
        if c in four_chars:
            continue
        if count_n_in(c, five_chars) == 3 and count_n_in(c, six_chars) == 3:
            return c


def determine_wire_mapping(wires_list):
    one = find_with_n_chars(wires_list, 2)
    seven = find_with_n_chars(wires_list, 3)

    char_to_segment = {
        "a": None,
        "b": None,
        "c": None,
        "d": None,
        "e": None,
        "f": None,
        "g": None,
    }

    char_to_segment[determine_segment_A(seven, one)] = "A"
    char_to_segment[determine_segment_B(wires_list)] = "B"
    char_to_segment[determine_segment_C(wires_list)] = "C"
    char_to_segment[determine_segment_D(wires_list)] = "D"
    char_to_segment[determine_segment_E(wires_list)] = "E"
    char_to_segment[determine_segment_F(wires_list)] = "F"
    char_to_segment[determine_segment_G(wires_list)] = "G"

    return char_to_segment


def determine_output_values(values_list, wire_mapping):
    segments = []
    for v in values_list:
        digit = ""
        for c in v:
            digit += wire_mapping[c]

        segments.append(digit)

    output_values = list(
        map(lambda x: SEGMENTS_TO_DIGITS["".join(sorted(x))], segments)
    )

    output_value = (
        (1000 * output_values[0])
        + (100 * output_values[1])
        + (10 * output_values[2])
        + output_values[3]
    )

    return output_value


if __name__ == "__main__":

    with open("day_eight/input.txt") as f:
        lines = f.readlines()

    output_values = []
    full_io = []
    n_chars = []
    totals = []
    for line in lines:
        ov = line.split("|")[-1].strip().split(" ")
        wire = line.split("|")[0].strip().split(" ")
        output_values.append(ov)
        chars = list(map(lambda x: len(x), ov))
        full_io.append((wire, ov))

        # part two
        wire_to_segment_mapping = determine_wire_mapping(wire)
        output_value = determine_output_values(ov, wire_to_segment_mapping)
        totals.append(output_value)

    print(output_values)
    unique_chars = [2, 4, 3, 7]
    print(np.isin(np.array(n_chars).flatten(), unique_chars).sum())

    print(np.sum(totals))
