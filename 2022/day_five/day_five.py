from queue import LifoQueue
from collections import deque
from collections import namedtuple

instruction = namedtuple("instruction", ["n_move", "from_stack", "to_stack"])


def read_stacks(path):
    with open(path, "r") as f:
        lines = f.readlines()

    lines.reverse()
    line_length = len(lines[0])
    n_lines = len(lines)
    stacks = {}
    line_poss = [i for i in range(1, line_length, 4)]
    # initialise stacks
    for lp in line_poss:
        stacks[line_poss.index(lp) + 1] = deque()
    for n in range(1, n_lines):
        line = lines[n]
        for lp in line_poss:
            if line[lp] != " ":
                stacks[line_poss.index(lp) + 1].append(line[lp])

    return stacks


def read_instructions(path):
    with open(path, "r") as f:
        lines = f.readlines()
    instructions = []
    for line in lines:
        l_s = line.split(" ")
        instructions.append(instruction(int(l_s[1]), int(l_s[3]), int(l_s[5])))

    return instructions


def process_instruction(stacks, instruct):
    for _ in range(0, instruct.n_move):
        stacks[instruct.to_stack].append(stacks[instruct.from_stack].pop())

    return stacks


def process_instruction_p2(stacks, instruct):
    move_list = []
    try:
        for _ in range(0, instruct.n_move):
            move_list.append(stacks[instruct.from_stack].pop())
    except:
        print("hello world")

    move_list.reverse()
    if len(move_list) == 1:
        stacks[instruct.to_stack].append(move_list[0])
    else:
        stacks[instruct.to_stack].extend(move_list)

    return stacks


if __name__ == "__main__":
    instructions = read_instructions(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_five/input_instr.txt"
    )
    stacks = read_stacks(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_five/input_stacks.txt"
    )

    for inst in instructions:
        stacks = process_instruction(stacks, inst)

    top_letters = []
    for i, val in stacks.items():
        letter = val.pop()
        top_letters.append(letter)
        print(f"{i} {letter}")

    print("".join(top_letters))

    print("hello_world")

    instructions = read_instructions(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_five/input_instr.txt"
    )
    stacks = read_stacks(
        "/Users/TimothyW/Fun/avent_of_code/2022/day_five/input_stacks.txt"
    )

    for inst in instructions:
        stacks = process_instruction_p2(stacks, inst)

    top_letters = []
    for i, val in stacks.items():
        letter = val.pop()
        top_letters.append(letter)
        print(f"{i} {letter}")

    print("".join(top_letters))

    print("hello_world")
