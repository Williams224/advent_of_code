import numpy as np


def binary_array_to_decimal(arr):
    bin_str = ""
    for e in arr:
        bin_str = bin_str + str(e)
    print(bin_str)
    decimal = int(bin_str, 2)
    print(decimal)
    return decimal


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
