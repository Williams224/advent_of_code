import numpy as np
import itertools

from pathos.multiprocessing import ProcessingPool as Pool


class Instruction:
    def __init__(self, on_off, x_range, y_range, z_range):
        if on_off == "on":
            self.on_off = 1
        else:
            self.on_off = 0
        self.x_range = self.change_ints(x_range)
        self.y_range = self.change_ints(y_range)
        self.z_range = self.change_ints(z_range)

        self.n_cubes = (
            (self.x_range[1] - self.x_range[0])
            * (self.y_range[1] - self.y_range[0])
            * (self.z_range[1] - self.z_range[0])
        )

    def get_min_range(self):
        return min([self.x_range[0], self.y_range[0], self.z_range[0]])

    def get_max_range(self):
        return max([self.x_range[1], self.y_range[1], self.z_range[1]])

    def change_ints(self, range):
        return int(range[0]), int(range[1])

    def generate_cubes(self):
        return itertools.product(
            range(self.x_range[0], self.x_range[1] + 1),
            range(self.y_range[0], self.y_range[1] + 1),
            range(self.z_range[0], self.z_range[1] + 1),
        )


def read_instruction(line):
    line = line.strip("\n")
    inst_split = line.split(" ")
    on_off = inst_split[0]
    ranges = inst_split[-1].split(",")
    ranges = list(map(lambda x: x.split("=")[-1].split(".."), ranges))
    x_range = (ranges[0][0], ranges[0][1])
    y_range = (ranges[1][0], ranges[1][1])
    z_range = (ranges[2][0], ranges[2][1])
    return on_off, x_range, y_range, z_range


def instruction_filter(inst):
    if any([inst.x_range[0] < -50, inst.y_range[0] < -50, inst.z_range[0] < -50]):
        return False
    elif any([inst.x_range[1] > 50, inst.y_range[1] > 50, inst.z_range[1] > 50]):
        return False

    return True


class World:
    world = {}

    def __init__(self):
        print("created the world")

    def generate_cube_key(self, cube):
        return f"{cube[0]}_{cube[1]}_{cube[2]}"

    def apply_instruction(self, instruction):
        print(f" applying instruction with {instruction.n_cubes}")
        for c in instruction.generate_cubes():
            c_key = self.generate_cube_key(c)
            self.world[c_key] = instruction.on_off

    def get_n_on(self):
        return np.sum(list(self.world.values()))


if __name__ == "__main__":

    with open("day_twenty_two/input.txt") as f:
        lines = f.readlines()

    instruction_list = list(map(lambda x: Instruction(*read_instruction(x)), lines))

    # world_min = min(instruction_list, key=lambda k: k.get_min_range()).get_min_range()

    # world_max = max(instruction_list, key=lambda k: k.get_max_range()).get_max_range()

    # print(f"world min = {world_min}")

    # print(f"world min = {world_max}")

    p = Pool(14)

    world = World()

    # p.map(world.apply_instruction, instruction_list)

    n = len(instruction_list)
    for i in range(0, n):
        if i % 10 == 0:
            print(f"done {i} of {n} instructions")
        world.apply_instruction(instruction_list[i])

    print(world.get_n_on())

    print("end")