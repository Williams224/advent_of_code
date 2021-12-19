from functools import reduce
from itertools import product

import numpy as np


class SnailFishNum:
    def __init__(self, num_string=None, vals=None, nests=None):
        if num_string:
            self.vals, self.nests = self._ingest(num_string)
        elif vals and nests:
            self.vals = vals
            self.nests = nests

    def _ingest(self, s):
        l_s = list(s)
        vals = []
        nest_level = []
        curr_nest_level = 0
        for c in l_s:
            if c == " " or c == ",":
                continue
            elif c == "[":
                curr_nest_level += 1
            elif c == "]":
                curr_nest_level -= 1
            else:
                vals.append(int(c))
                nest_level.append(curr_nest_level)

        return vals, nest_level

    def _addition(self, other_vals, other_nests):
        new_vals = self.vals + other_vals
        new_nests = self.nests + other_nests
        new_nests = list(map(lambda x: x + 1, new_nests))
        return SnailFishNum(vals=new_vals, nests=new_nests)

    def __add__(self, other):
        self._addition(other.vals, other.nests)
        ret_fish = self._addition(other.vals, other.nests)
        ret_fish.redu()
        return ret_fish

    def pairs_left(self, nests):
        for i in range(0, len(nests) - 2):
            if nests[i] == nests[i + 1]:
                return True

        return False

    def magnitude(self, tmp_vals=None, tmp_nests=None):
        if tmp_vals == None and tmp_nests == None:
            tmp_vals = self.vals
            tmp_nests = self.nests
        while len(tmp_vals) > 2:
            i = 0
            while i < len(tmp_vals):
                if i < len(tmp_vals) - 1:
                    # in a pair
                    if tmp_nests[i] == tmp_nests[i + 1]:
                        new_val = 3 * tmp_vals[i] + 2 * tmp_vals[i + 1]
                        new_nest = tmp_nests[i] - 1
                        del tmp_nests[i : i + 2]
                        del tmp_vals[i : i + 2]
                        tmp_vals.insert(i, new_val)
                        tmp_nests.insert(i, new_nest)
                        i += 1
                    else:
                        i += 1
                else:
                    i += 1
        return 3 * tmp_vals[0] + 2 * tmp_vals[1]

    def redu(self):
        if self.explode():
            return self.redu()
        elif self.split():
            return self.redu()
        else:
            return None

    def explode(self):
        for i in range(0, len(self.vals)):
            if self.nests[i] > 4:
                h = self.nests[i]
                if i > 0:
                    self.vals[i - 1] += self.vals[i]
                if i < len(self.vals) - 2:
                    self.vals[i + 2] += self.vals[i + 1]
                del self.vals[i : i + 2]
                del self.nests[i : i + 2]
                self.vals.insert(i, 0)
                self.nests.insert(i, h - 1)
                return True

        return False

    def split(self):
        for i in range(0, len(self.vals)):
            if self.vals[i] >= 10:
                p_left = int(self.vals[i] / 2)
                p_right = self.vals[i] - p_left
                del self.vals[i]
                self.vals.insert(i, p_left)
                self.vals.insert(i + 1, p_right)
                original_n = self.nests[i]
                del self.nests[i]
                self.nests.insert(i, original_n + 1)
                self.nests.insert(i + 1, original_n + 1)
                return True

        return False


def get_max_combination(a, b):
    # comb_one = (a + b).magnitude()
    comb_two = (b + a).magnitude()
    return max(comb_one, comb_two)


if __name__ == "__main__":

    import sys

    sys.setrecursionlimit(10000)
    print(sys.getrecursionlimit())

    with open("day_eighteen/input.txt") as f:
        lines = f.readlines()

        snf_list = list(map(lambda x: SnailFishNum(x.strip("\n")), lines))

        result = reduce(lambda a, b: a + b, snf_list).magnitude()
        print(result)

        print("part two")

        combinations = list(product(snf_list, snf_list))

        combination_23 = combinations[23][1] + combinations[23][0]
        print("H")
        curr_max = 0
        for i in range(0, len(combinations)):
            if i % 10 == 0:
                print(f"_____{i}_____")

            if i == 23:
                continue
            a, b = combinations[i]
            max_comb = get_max_combination(a, b)
            if max_comb > curr_max:
                curr_max = max_comb

        print(f"max comb overall = {curr_max}")
