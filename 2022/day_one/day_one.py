import pandas as pd
import numpy as np

if __name__ == "__main__":

    elves = []
    with open("/Users/TimothyW/Fun/avent_of_code/2022/day_one/input.txt", "r") as f:
        elf = []
        for line in f.readlines():
            if line == "\n":
                elves.append(elf)
                elf = []
            else:
                elf.append(int(line.rstrip("\n")))

    totals = list(map(np.sum, elves))
    print(f"total = ", np.max(totals))

    totals.sort()

    top_three_elves = totals[-1] + totals[-2] + totals[-3]
    print(top_three_elves)
    print("h")
