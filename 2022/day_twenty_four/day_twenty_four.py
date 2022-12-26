import numpy as np

# for each round
# consider possible moved
# launch recursive function in that direction
# if coords = end return n_steps

# new encoding ^ = 1 > = 10 v = 100 < = 1000


def read_input(path):
    with open(path, "r") as f:
        lines = list(map(lambda x: x.strip("\n"), f.readlines()))

    world_map = []
    for line in lines:
        world_map.append(list(line))

    return np.array(world_map)


def encode_char(c):
    if c == "^":
        return 1
    elif c == ">":
        return 10
    elif c == "v":
        return 100
    elif c == "<":
        return 1000
    elif c == "#":
        return -1
    elif c == ".":
        return 0


class World:
    def __init__(self, char_map):
        self.map_shape = char_map.shape
        self.world_map = np.zeros(self.map_shape)
        for y in range(0, self.map_shape[0]):
            for x in range(0, self.map_shape[1]):
                self.world_map[y, x] += encode_char(char_map[y, x])

    def calc_future_map(self, old_map):
        new_map = np.zeros(self.map_shape)
        for y in range(0, self.map_shape[0]):
            for x in range(0, self.map_shape[1]):
                old_val = old_map[y, x]
                if old_val <= 0:
                    new_map[y, x] = old_val
                elif old_val < 10:
                    new_x = x
                    new_y = y - 1
                    if new_y < 1:
                        new_y = self.map_shape[0] - 2
                    new_map[new_y, new_x] += old_val
                elif old_val < 100:
                    

    def take_step(self):
        pass


if __name__ == "__main__":

    char_map = read_input(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_twenty_four/test_input.txt"
    )

    starting_position = (0, 1)

    world = World(char_map)
    print(char_map)
