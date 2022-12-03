import pandas as pd
import numpy as np

# A = Rock
# B = Paper
# C = scissors
# X = Rock
# Y = Paper
# Z = scissors

# Rock > scissors
# scissors > paper
# paper > Rock
# 1 > 3
# 3 > 2
# 2 > 1
# 0 = lose
# 3 = Draw
# 6 = win

# X = lose, y= draw, z = win


def deterimine_win(row):
    opponent = row["opponent"]
    me = row["me"]
    if me == "X":
        me_normed = "A"
    elif me == "Y":
        me_normed = "B"
    elif me == "Z":
        me_normed = "C"

    if me_normed == opponent:
        return 3
    if me_normed == "A":
        if opponent == "C":
            return 6
        if opponent == "B":
            return 0

    if me_normed == "B":
        if opponent == "A":
            return 6
        if opponent == "C":
            return 0

    if me_normed == "C":
        if opponent == "B":
            return 6
        if opponent == "A":
            return 0


def determine_required_choice(row):
    opponent = row["opponent"]
    me = row["me"]
    if me == "Y":
        return opponent
    if me == "X":
        if opponent == "A":
            return "C"
        if opponent == "B":
            return "A"
        if opponent == "C":
            return "B"
    if me == "Z":
        if opponent == "A":
            return "B"
        if opponent == "B":
            return "C"
        if opponent == "C":
            return "A"


if __name__ == "__main__":
    df = pd.read_csv(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_two/input.txt", sep=" ", header=None
    )
    df.columns = ["opponent", "me"]

    df["win_points"] = df.apply(deterimine_win, axis=1)
    df["selection_points"] = np.select(
        [df.me == "X", df.me == "Y", df.me == "Z"], [1, 2, 3]
    )
    df["total_points"] = df["win_points"] + df["selection_points"]
    df["part_two_win_points"] = np.select(
        [df.me == "X", df.me == "Y", df.me == "Z"], [0, 3, 6]
    )
    df["part_two_required_choice"] = df.apply(determine_required_choice, axis=1)
    df["part_two_choice_points"] = np.select(
        [
            df.part_two_required_choice == "A",
            df.part_two_required_choice == "B",
            df.part_two_required_choice == "C",
        ],
        [1, 2, 3],
    )

    df["part_two_total_points"] = (
        df["part_two_win_points"] + df["part_two_choice_points"]
    )
    print("hello")
