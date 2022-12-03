import numpy as np
import math


def binary_array_to_decimal(arr):
    bin_str = ""
    for e in arr:
        bin_str = bin_str + str(e)
    print(bin_str)
    decimal = int(bin_str, 2)
    print(decimal)
    return decimal


def get_rating(array, position, rating):
    assert rating == "oxygen" or rating == "c02"
    if len(array) == 1:
        return array
    sums = np.sum(array, axis=0)
    mode_threshold = math.floor(array.shape[0] / 2)
    if rating == "oxygen":
        modes = (sums >= mode_threshold).astype(int)
    else:
        modes = (sums < mode_threshold).astype(int)
    print(position, len(array[array[:, position] == modes[position]]))

    return get_rating(
        array[array[:, position] == modes[position]], position + 1, rating
    )


if __name__ == "__main__":
    input = np.loadtxt("day_three/input.txt", dtype=str)
    input_split = [list(n) for n in input]
    a = np.array(input_split).astype(int)
    print(a.shape)
    print(np.sum(a, axis=0))
    sums = np.sum(a, axis=0)
    gamma_bin = (sums > 500).astype(int)
    print(gamma_bin)
    epsilon_bin = (sums < 500).astype(int)
    gamma_dec = binary_array_to_decimal(gamma_bin)
    epsilon_dec = binary_array_to_decimal(epsilon_bin)

    print(gamma_dec * epsilon_dec)

    oxygen_rating_bin = get_rating(a, 0, "oxygen")
    c02_rating_bin = get_rating(a, 0, "c02")
    print(oxygen_rating_bin)
    print(c02_rating_bin)
    oxygen_rating_dec = binary_array_to_decimal(oxygen_rating_bin[0])
    c02_rating_dec = binary_array_to_decimal(c02_rating_bin[0])
    print(oxygen_rating_dec * c02_rating_dec)