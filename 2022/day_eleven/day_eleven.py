from math import log, exp

# 17040359


class Item:
    mods = [23, 19, 13, 17, 7, 11, 13, 3, 17, 2, 5, 19]

    def __init__(self, init_value):
        self.init_value = init_value
        self.mod_dict = {}
        for i in self.mods:
            self.mod_dict[i] = self.init_value % i

    def apply_operation(self, operation_func):
        for k, v in self.mod_dict.items():
            self.mod_dict[k] = operation_func(k, v)


class Monkey:
    def __init__(
        self, index, item_vals, operation, test_val, true_monkey, false_monkey
    ):
        self.index = index
        self.items = [Item(i) for i in item_vals]
        self.operation = operation
        self.test_val = test_val
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.operation_func = None
        self.total_inspections = 0

    def inspect_item(self):
        self.total_inspections += 1
        item = self.items.pop(0)
        if self.operation_func is None:
            raise ValueError()
        else:
            item.apply_operation(self.operation_func)

        if item.mod_dict[self.test_val] == 0:
            return item, self.true_monkey
        else:
            return item, self.false_monkey

    def take_turn(self):
        throw_list = []
        for i in range(0, len(self.items)):
            item, monkey = self.inspect_item()
            throw_list.append((item, monkey))

        return throw_list

    def catch_item(self, value):
        self.items.append(value)


def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines = [line.strip("\n") for line in lines]

    line_iter = iter(lines)
    monkeys = []
    while True:
        monkey_title = next(line_iter, None)
        if monkey_title is None:
            break
        monkey_index = int(monkey_title.split(" ")[1].strip(":"))
        items_list_str = next(line_iter)
        items_list = [
            int(l.strip(" ")) for l in items_list_str.split(":")[1].split(",")
        ]
        operation_str = next(line_iter)
        operation = operation_str.split(":")[1].strip(" ")
        test_str = next(line_iter)
        test = int(test_str.split(":")[1].split(" ")[-1])
        true_monkey_str = next(line_iter)
        true_monkey = int(true_monkey_str.split(" ")[-1])
        false_monkey_str = next(line_iter)
        false_monkey = int(false_monkey_str.split(" ")[-1])

        monkeys.append(
            Monkey(monkey_index, items_list, operation, test, true_monkey, false_monkey)
        )
        if next(line_iter, None) is None:
            break

    return monkeys


def square_it(x):
    # print("square", x)
    return x * x


def modular_add(m, a_mod_m, add):
    return (a_mod_m + (add % m)) % m


def modular_multiply(m, a_mod_m, multiple):
    return (a_mod_m * (multiple % m)) % m


def modular_exponent(m, a_mod_m, exponent):
    return (a_mod_m ** exponent) % m


if __name__ == "__main__":

    monkeys = read_input("/Users/TimothyW/Fun/avent_of_code/2022/day_eleven/input.txt")

    # Item is a class which has a mod value for all mods we try, created on initialisation.
    # Takes lambda to apply to items.

    monkeys[0].operation_func = lambda m, a_mod_m: modular_multiply(m, a_mod_m, 11)
    monkeys[1].operation_func = lambda m, a_mod_m: modular_add(m, a_mod_m, 1)
    monkeys[2].operation_func = lambda m, a_mod_m: modular_multiply(m, a_mod_m, 7)
    monkeys[3].operation_func = lambda m, a_mod_m: modular_add(m, a_mod_m, 3)
    monkeys[4].operation_func = lambda m, a_mod_m: modular_add(m, a_mod_m, 6)
    monkeys[5].operation_func = lambda m, a_mod_m: modular_add(m, a_mod_m, 5)
    monkeys[6].operation_func = lambda m, a_mod_m: modular_exponent(m, a_mod_m, 2)
    monkeys[7].operation_func = lambda m, a_mod_m: modular_add(m, a_mod_m, 7)

    prev_monkey_business = 0
    for i in range(1, 10001):
        for monkey in monkeys:
            # print("starting monkey")
            throw_list = monkey.take_turn()
            for item in throw_list:
                monkeys[item[1]].catch_item(item[0])

        monkeys_c = monkeys.copy()
        monkeys_c.sort(key=lambda m: m.total_inspections)
        monkey_business = (
            monkeys_c[-1].total_inspections * monkeys_c[-2].total_inspections
        )
        print(i)
        for m in monkeys:
            print(m.index, m.total_inspections)

    print(monkey_business)
