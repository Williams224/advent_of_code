import numpy as np


def load_map(file):
    with open(file) as f:
        lines = f.readlines()

    lines = [list(l.strip("\n")) for l in lines]

    return np.array(lines, dtype=int)


def increment_flasher(row, col, map):
    if row <= 9 and row >= 0 and col >= 0 and col <= 9:
        map[row][col] += 1

    return map


def check_and_flash(row, col, map, step_flashed_indices, total_flashes):
    if row <= 9 and row >= 0 and col >= 0 and col <= 9:
        if map[row][col] > 9 and ((row, col) not in step_flashed_indices):
            step_flashed_indices.append((row, col))
            vals_to_check = []
            # up
            vals_to_check.append((row - 1, col))
            # down
            vals_to_check.append((row + 1, col))
            # right
            vals_to_check.append((row, col + 1))
            # left
            vals_to_check.append((row, col - 1))
            # dl
            vals_to_check.append((row + 1, col - 1))
            # dr
            vals_to_check.append((row + 1, col + 1))
            # ur
            vals_to_check.append((row - 1, col + 1))
            vals_to_check.append((row - 1, col - 1))
            for r, c in vals_to_check:
                map = increment_flasher(r, c, map)
            map[row][col] = 0
            total_flashes += 1
    return total_flashes


if __name__ == "__main__":
    map = load_map("day_eleven/input.txt")
    total_flashes = 0
    for s in range(0, 1000):
        step_flashed_indices = []
        map = map + 1
        while np.sum(map > 9) != 0:
            for row in range(0, 10):
                for col in range(0, 10):
                    total_flashes = check_and_flash(
                        row, col, map, step_flashed_indices, total_flashes
                    )

            for r, c in step_flashed_indices:
                map[r][c] = 0

        total_step_flashes = np.sum(map == 0)
        if total_step_flashes == 100:
            print("next sync step = ", s)
            break

    print(map)
    print(total_flashes)
