import numpy as np

CLOSE_OPEN_DICT = {"}": "{", ")": "(", "]": "[", ">": "<"}
OPENING_CHARS = {"{", "[", "<", "("}
OPEN_CLOSE_DICT = {"{": "}", "(": ")", "[": "]", "<": ">"}
SCORE_DICT = {")": 3, "]": 57, "}": 1197, ">": 25137}


def is_line_corrupt(line):
    line_list = list(line)
    opening_chars = []
    for c in line_list:
        if len(opening_chars) > 0:
            possible_closing_char = OPEN_CLOSE_DICT[opening_chars[-1]]
        else:
            possible_closing_char = None
        print(" c char determined")
        if c in OPENING_CHARS:
            opening_chars.append(c)
        elif c != possible_closing_char:
            return True, c
        else:
            del opening_chars[-1]

    return False, None


def find_closing_chars(line):
    line_list = list(line)
    opening_chars = []
    for c in line_list:
        if c in OPENING_CHARS:
            opening_chars.append(c)
        else:
            del opening_chars[-1]

    req_closing_chars = [OPEN_CLOSE_DICT[c] for c in reversed(opening_chars)]
    return req_closing_chars


COMPLETION_DICT = {")": 1, "]": 2, "}": 3, ">": 4}


def get_completion_score(comp_chars):
    score = 0
    for c in comp_chars:
        score *= 5
        score += COMPLETION_DICT[c]

    return score


if __name__ == "__main__":

    with open("day_ten/input.txt", "r") as f:
        tmp_lines = f.readlines()
    lines = [t.strip("\n") for t in tmp_lines]
    offending_chars = []
    legit_lines = []
    for line in lines:
        result, offending_char = is_line_corrupt(line)
        if result:
            offending_chars.append(offending_char)
        else:
            legit_lines.append(line)

    total = 0
    values, counts = np.unique(offending_chars, return_counts=True)

    for v, c in zip(values, counts):
        total += SCORE_DICT[v] * c

    print(total)

    completion_scores = []
    for ll in legit_lines:
        completion_scores.append(get_completion_score(find_closing_chars(ll)))

    print(completion_scores)

    print(np.median(completion_scores))
