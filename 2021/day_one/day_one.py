import numpy as np
import pandas as pd


def n_larger(arr):
    return (np.insert(arr[:-1], 0, np.nan) < arr).sum()


if __name__ == "__main__":
    a = np.loadtxt("day_one/input.txt")
    print(n_larger(a))

    s = pd.Series(a)
    n_window_larger = n_larger(s.rolling(3, min_periods=3).sum().values)
    print(n_window_larger)
