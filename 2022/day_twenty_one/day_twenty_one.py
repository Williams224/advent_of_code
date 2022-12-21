from scipy.optimize import fsolve


def load_input(path):
    with open(path, "r") as f:
        lines = f.readlines()

    return [line.strip("\n") for line in lines]


class MonkeyFinder:
    def __init__(self, monkey_dict, humn=None):
        self.monkey_dict = monkey_dict
        self.instructions = []
        if humn:
            monkey_dict["humn"] = humn

    def find_value_monkey(self, monkey_name):
        val = self.monkey_dict[monkey_name]
        if type(val) == int:
            return val
        else:
            if "+" in val:
                monkeys = list(map(lambda x: x.strip(), val.split("+")))
                self.instructions.append(val)
                return self.find_value_monkey(monkeys[0]) + self.find_value_monkey(
                    monkeys[1]
                )
            if "-" in val:
                monkeys = list(map(lambda x: x.strip(), val.split("-")))
                self.instructions.append(val)
                return self.find_value_monkey(monkeys[0]) - self.find_value_monkey(
                    monkeys[1]
                )
            if "*" in val:
                monkeys = list(map(lambda x: x.strip(), val.split("*")))
                self.instructions.append(val)
                return self.find_value_monkey(monkeys[0]) * self.find_value_monkey(
                    monkeys[1]
                )
            if "/" in val:
                monkeys = list(map(lambda x: x.strip(), val.split("/")))
                self.instructions.append(val)
                return self.find_value_monkey(monkeys[0]) / self.find_value_monkey(
                    monkeys[1]
                )


if __name__ == "__main__":

    inputs = load_input(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_twenty_one/input.txt"
    )
    operators = ["+", "-", "*", "/"]
    monkey_dict = {}
    for input in inputs:
        key = input.split(":")[0].strip()
        value = input.split(":")[-1].strip()
        is_instruction = False
        for o in operators:
            if o in value:
                is_instruction = True
                break
        if not is_instruction:
            value = int(value)
        monkey_dict[key] = value

    monkey_dict["humn"] = -999
    mf = MonkeyFinder(monkey_dict)

    # need to make lccz = 21973580688943
    """nput =  3910000000000 result =  22021175632644.152"""
    """input =  3920000000000 result =  21947852175854.016"""
    for i in range(3916491093631, 3916491093831, 1):
        input = i
        mf2 = MonkeyFinder(monkey_dict, input)
        result = mf2.find_value_monkey("lccz")
        diff = result - 21973580688943
        print(diff)
        if diff == 0:
            print(i)
            break
        print("input = ", input, "result = ", result)
