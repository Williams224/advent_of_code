import numpy as np


def natural_sum(x):
    return x * (x + 1) / 2.0


if __name__ == "__main__":
    with open("day_seven/input.txt") as f:
        input = np.array(f.read().split(","), dtype=int)

    print(input)

    total_fuel_costs = []
    total_fuel_costs_part_two = []
    for i in range(0, 2000):
        fuel_cost = np.abs(input - i)
        total_fuel_costs.append(np.sum(fuel_cost))
        total_fuel_costs_part_two.append(
            np.sum(np.array(list(map(natural_sum, fuel_cost))))
        )

    print(total_fuel_costs)
    print(np.min(total_fuel_costs))
    print(np.min(total_fuel_costs_part_two))
