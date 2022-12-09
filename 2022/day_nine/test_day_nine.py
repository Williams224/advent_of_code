import unittest
from .day_nine import Knot, Head, Tail


class testDayNine(unittest.TestCase):
    def test_movement(self):
        knot = Knot("test_knot", (0, 0))

        knot.move("R 4")
        self.assertTupleEqual(knot.position, (4, 0))
        knot.move("U 5")
        self.assertTupleEqual(knot.position, (4, 5))
        knot.move("D 6")
        self.assertTupleEqual(knot.position, (4, -1))
        knot.move("L 1")
        self.assertTupleEqual(knot.position, (3, -1))

        tail = Tail("test_tail", (0, 0))
        head = Head("test_head", (0, 0), tail)

        head.move("R 2")
        self.assertTupleEqual(head.position, (2, 0))
        self.assertTupleEqual(head.tail.position, (1, 0))
        head.move("U 3")
        self.assertTupleEqual(head.position, (2, 3))
        self.assertTupleEqual(head.tail.position, (2, 2))
        head.move("D 2")
        self.assertTupleEqual(head.position, (2, 1))
        self.assertTupleEqual(head.tail.position, (2, 2))
        head.move("L 1")
        self.assertTupleEqual(head.position, (1, 1))
        self.assertTupleEqual(head.tail.position, (2, 2))
