import numpy as np
import uuid
from itertools import cycle, islice


def read_input(path):
    with open(path, "r") as f:
        lines = list(map(lambda l: l.strip("\n"), f.readlines()))

    elf_coordinates = []
    for i in range(0, len(lines)):
        for c in range(0, len(lines[i])):
            if lines[i][c] == "#":
                elf_coordinates.append((int(i), int(c)))
    return elf_coordinates


class Elf:
    elf_catalog = {}

    def __init__(self, coords):
        self.coords = coords
        self.id = str(uuid.uuid4())
        self.elf_catalog[self.id] = self.coords

    def check_surroundings(self):
        y = self.coords[0]
        x = self.coords[1]

        self.check_poses = {
            "n": (y - 1, x),
            "ne": (y - 1, x + 1),
            "e": (y, x + 1),
            "se": (y + 1, x + 1),
            "s": (y + 1, x),
            "sw": (y + 1, x - 1),
            "w": (y, x - 1),
            "nw": (y - 1, x - 1),
        }
        other_poses = set(self.elf_catalog.values())
        self.filled = {}
        for dir, coord in self.check_poses.items():
            self.filled[dir] = coord in other_poses

    def propose_move(self, prio_list):
        self.check_surroundings()
        if not any(self.filled.values()):
            return True, self.coords

        for direction in prio_list:
            if direction == "n":
                if not any([self.filled["n"], self.filled["ne"], self.filled["nw"]]):
                    return False, self.check_poses["n"]
            if direction == "s":
                if not any([self.filled["s"], self.filled["se"], self.filled["sw"]]):
                    return False, self.check_poses["s"]
            if direction == "w":
                if not any([self.filled["w"], self.filled["nw"], self.filled["sw"]]):
                    return False, self.check_poses["w"]
            if direction == "e":
                if not any([self.filled["e"], self.filled["ne"], self.filled["se"]]):
                    return False, self.check_poses["e"]

        return True, self.coords

    def move(self, new_coord):
        if new_coord == None:
            return None
        self.coords = new_coord
        self.elf_catalog[self.id] = new_coord


def draw(elves):
    map = np.zeros((15, 15))
    for elf in elves:
        x = elf.coords[1]
        y = elf.coords[0]
        map[y][x] = 1

    st_map = np.empty((15, 15), dtype=str)
    st_map[map == 1] = "#"
    st_map[map == 0] = "."

    print(np.array2string(st_map))


if __name__ == "__main__":
    elf_poses = read_input(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_twenty_two/input.txt"
    )

    elves = [Elf(e) for e in elf_poses]

    move_options = ["n", "s", "w", "e"]
    first_round_number = 1
    for round_n in range(first_round_number, 1000):
        proposed_moves = {}
        print("____", round_n, "_____")
        # print(move_options)
        move_not_req_list = []
        for elf in elves:
            move_not_req, proposed_moves[elf.id] = elf.propose_move(move_options)
            move_not_req_list.append(move_not_req)
        print(sum(move_not_req_list))
        if all(move_not_req_list):
            print(f"No moves required {round_n}")
            break

        pm_list = list(proposed_moves.values())
        duplicate_moves = set([x for x in pm_list if pm_list.count(x) > 1])

        for id, pm in proposed_moves.items():
            if pm in duplicate_moves:
                proposed_moves[id] = None

        for elf in elves:
            new_coord = proposed_moves[elf.id]
            elf.move(new_coord)
        # print(f"______________{round_n}_______________")
        # draw(elves)
        move_options.append(move_options.pop(0))

    min_y = min(elves, key=lambda x: x.coords[0]).coords[0]
    max_y = max(elves, key=lambda x: x.coords[0]).coords[0]
    min_x = min(elves, key=lambda x: x.coords[1]).coords[1]
    max_x = max(elves, key=lambda x: x.coords[1]).coords[1]

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    empty_squares = width * height - len(elves)

    print("end")