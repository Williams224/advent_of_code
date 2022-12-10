import unittest
from .day_ten import Register
from collections import deque


class testDayTen(unittest.TestCase):
    def setUp(self) -> None:
        with open(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_ten/test_input.txt", "r"
        ) as f:
            lines = f.readlines()
        self.instructions = [line.strip("\n") for line in lines]
        self.queue = deque()
        for inst in self.instructions:
            split_inst = inst.split(" ")
            if split_inst[0] == "noop":
                self.queue.appendleft({"oper": split_inst[0], "cycles_left": 1})
            elif split_inst[0] == "addx":
                self.queue.appendleft(
                    {"oper": "addx", "val": int(split_inst[1]), "cycles_left": 2}
                )
        self.register = Register(self.queue)
        return super().setUp()

    def test_cycle(self):
        while self.register.instruction_queue:
            self.register.cycle()

        self.assertEqual(self.register.get_signal_strength(20), 420)
        self.assertEqual(self.register.get_signal_strength(60), 1140)
        self.assertEqual(self.register.get_signal_strength(100), 1800)
        self.assertEqual(self.register.get_signal_strength(140), 2940)
        self.assertEqual(self.register.get_signal_strength(180), 2880)
        self.assertEqual(self.register.get_signal_strength(220), 3960)
