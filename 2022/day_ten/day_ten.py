from collections import deque
import numpy as np


class Register:
    def __init__(self, queue, init_val=1):
        self.value = init_val
        self.cycle_hist = []
        self.instruction_queue = queue
        self.current_instruction = None

    def cycle(self):
        self.cycle_hist.append(self.value)
        if self.current_instruction is None:
            self.current_instruction = self.instruction_queue.pop()

        self.current_instruction["cycles_left"] -= 1
        if self.current_instruction["cycles_left"] > 0:
            return
        elif self.current_instruction["cycles_left"] == 0:
            inst = self.current_instruction["oper"]
            if inst == "addx":
                self.value += self.current_instruction["val"]
            self.current_instruction = None
            return

    def get_signal_strength(self, cycle_n):
        reg_value = self.cycle_hist[cycle_n - 1]
        return reg_value * cycle_n


def determine_pixel(draw_position, sprite_position):
    draw_x = draw_position % 40
    if np.abs(sprite_position - draw_x) <= 1:
        return "#"
    else:
        return "."


if __name__ == "__main__":

    with open("/Users/TimothyW/Fun/avent_of_code/2022/day_ten/input.txt", "r") as f:
        lines = f.readlines()
    instructions = [line.strip("\n") for line in lines]
    queue = deque()
    for inst in instructions:
        split_inst = inst.split(" ")
        if split_inst[0] == "noop":
            queue.appendleft({"oper": split_inst[0], "cycles_left": 1})
        elif split_inst[0] == "addx":
            queue.appendleft(
                {"oper": "addx", "val": int(split_inst[1]), "cycles_left": 2}
            )

    register = Register(queue)

    pixels = []
    pixel_i = 0
    while register.instruction_queue:

        sprite_position = register.value
        to_draw = determine_pixel(pixel_i, sprite_position)
        pixels.append(to_draw)
        register.cycle()

        pixel_i += 1

    strengths = []
    for i in [20, 60, 100, 140, 180, 220]:
        signal_strength = register.get_signal_strength(i)
        print(f"signal strenght for cycle {i} = {signal_strength}")
        strengths.append(signal_strength)

    rows = np.split(np.array(pixels), 6)
    print(" ".join(rows[0]))
    print(" ".join(rows[1]))
    print(" ".join(rows[2]))
    print(" ".join(rows[3]))
    print(" ".join(rows[4]))
    print(" ".join(rows[5]))
    print("hellow world")
