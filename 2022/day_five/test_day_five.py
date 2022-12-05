import unittest
from queue import LifoQueue
from .day_five import (
    read_stacks,
    read_instructions,
    process_instruction,
    process_instruction_p2,
)


def queue_to_list(qu):
    l = list(qu)
    l.reverse()
    return l


"""move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

# chars at 1,5,9
class TestInput(unittest.TestCase):
    def test_read_stacks(self):
        stacks = read_stacks(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_five/test_input_stacks.txt"
        )

        self.assertListEqual(queue_to_list(stacks[1]), ["N", "Z"])
        self.assertListEqual(queue_to_list(stacks[2]), ["D", "C", "M"])
        self.assertListEqual(queue_to_list(stacks[3]), ["P"])

    def test_read_instructions(self):
        instructions = read_instructions(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_five/test_input_inst.txt"
        )

        self.assertEqual(instructions[0].n_move, 1)
        self.assertEqual(instructions[1].n_move, 3)
        self.assertEqual(instructions[2].n_move, 2)
        self.assertEqual(instructions[3].n_move, 1)
        self.assertEqual(instructions[0].from_stack, 2)
        self.assertEqual(instructions[1].from_stack, 1)
        self.assertEqual(instructions[2].from_stack, 2)
        self.assertEqual(instructions[3].from_stack, 1)
        self.assertEqual(instructions[0].to_stack, 1)
        self.assertEqual(instructions[1].to_stack, 3)
        self.assertEqual(instructions[2].to_stack, 1)
        self.assertEqual(instructions[3].to_stack, 2)


class TestProcessInstruction(unittest.TestCase):
    def setUp(self) -> None:
        self.stacks = read_stacks(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_five/test_input_stacks.txt"
        )
        self.instructions = read_instructions(
            "/Users/TimothyW/Fun/avent_of_code/2022/day_five/test_input_inst.txt"
        )
        return super().setUp()

    def test_process_instruction(self):
        actual_stacks = process_instruction(self.stacks, self.instructions[0])
        self.assertListEqual(queue_to_list(actual_stacks[1]), ["D", "N", "Z"])
        self.assertListEqual(queue_to_list(actual_stacks[2]), ["C", "M"])
        print('hello"')

    def test_process_instruction_p2(self):
        actual_stacks = process_instruction_p2(self.stacks, self.instructions[0])
        self.assertListEqual(queue_to_list(actual_stacks[1]), ["D", "N", "Z"])
        self.assertListEqual(queue_to_list(actual_stacks[2]), ["C", "M"])

        actual_stacks = process_instruction_p2(actual_stacks, self.instructions[1])
        self.assertListEqual(queue_to_list(actual_stacks[1]), [])
        print(actual_stacks[3])
        self.assertListEqual(queue_to_list(actual_stacks[2]), ["C", "M"])
        self.assertListEqual(queue_to_list(actual_stacks[3]), ["D", "N", "Z", "P"])

        actual_stacks = process_instruction_p2(actual_stacks, self.instructions[2])
        self.assertListEqual(queue_to_list(actual_stacks[1]), ["C", "M"])
        self.assertListEqual(queue_to_list(actual_stacks[2]), [])
        self.assertListEqual(queue_to_list(actual_stacks[3]), ["D", "N", "Z", "P"])

        actual_stacks = process_instruction_p2(actual_stacks, self.instructions[3])
        self.assertListEqual(queue_to_list(actual_stacks[1]), ["M"])
        self.assertListEqual(queue_to_list(actual_stacks[2]), ["C"])
        self.assertListEqual(queue_to_list(actual_stacks[3]), ["D", "N", "Z", "P"])
        print('hello"')
