import numpy as np


class FishPopulation:
    def __init__(self, fish_list):
        self.starting_fish_list = fish_list
        values, counts = np.unique(self.starting_fish_list, return_counts=True)
        self.population_counts = {x: 0 for x in range(0, 9)}
        for v, c in zip(values, counts):
            self.population_counts[v] += c

    def iterate_day(self):
        for v in range(0, 9):
            self.population_counts[v - 1] = self.population_counts[v]

        born = self.population_counts.pop(-1)
        self.population_counts[8] += born
        self.population_counts[6] += born
        print(self.population_counts)


if __name__ == "__main__":
    with open("day_dix/input.txt", "r") as f:
        all = f.read()

    starting_fish = np.array(all.split(","), dtype=int)

    world = FishPopulation(starting_fish)
    for i in range(0, 80):
        world.iterate_day()
        print(i)
        print(world.population_counts)
    print("h")
