import unittest
from functools import reduce

from day_eighteen.day_eighteen import SnailFishNum


class TestDayEighteen(unittest.TestCase):
    def setUp(self) -> None:
        self.sfn = SnailFishNum()
        self.explode_case_one = "[[[[[9, 8], 1], 2], 3], 4]"
        self.explode_case_two = "[7, [6, [5, [4, [3, 2]]]]]"  # [7,[6,[5,[7,0]]]]
        self.explode_case_three = "[[6, [5, [4, [3, 2]]]], 1]"
        self.explode_case_four = (
            "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"  # [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
        )

        self.split_case_one = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
        return super().setUp()

    def test_all(self):
        with open("day_eighteen/test_input.txt") as f:
            lines = f.readlines()

        snf_list = list(map(lambda x: SnailFishNum(x.strip("\n")), lines))
        self.assertEqual(reduce(lambda a, b: a + b, snf_list).magnitude(), 4140)

    def test_add_overload(self):
        sfn = SnailFishNum("[[[[4,3],4],4],[7,[[8,4],9]]]")
        sfn_two = SnailFishNum("[1,1]")
        sfn_result = sfn + sfn_two
        self.assertEqual(
            (sfn_result.vals, sfn_result.nests),
            ([0, 7, 4, 7, 8, 6, 0, 8, 1], [4, 4, 3, 4, 4, 4, 4, 2, 2]),
        )

        sfn_three = SnailFishNum("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
        sfn_four = SnailFishNum("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
        sfn_result = sfn_three + sfn_four
        sfn_expeced = SnailFishNum(
            "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"
        )
        self.assertEqual(
            (sfn_result.vals, sfn_result.nests), (sfn_expeced.vals, sfn_expeced.nests)
        )

    def test_magnitude(self):
        self.assertEqual(SnailFishNum("[[1,2],[[3,4],5]]").magnitude(), 143)
        self.assertEqual(
            SnailFishNum("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").magnitude(), 1384
        )
        self.assertEqual(SnailFishNum("[[[[1,1],[2,2]],[3,3]],[4,4]]").magnitude(), 445)
        self.assertEqual(SnailFishNum("[[[[3,0],[5,3]],[4,4]],[5,5]]").magnitude(), 791)
        self.assertEqual(
            SnailFishNum("[[[[5,0],[7,4]],[5,5]],[6,6]]").magnitude(), 1137
        )
        self.assertEqual(
            SnailFishNum(
                vals=[0, 8, 7, 6, 9, 0, 9, 9, 1, 3, 5],
                nests=[4, 4, 4, 4, 3, 4, 4, 4, 4, 3, 2],
            ).magnitude(),
            50,
        )

    def test_addition(self):
        sfn_one = SnailFishNum("[[8,[[8,6],[6,0]]],[8,[[1,8],1]]]")
        sfn_two = SnailFishNum("[[[9,1],3],5]")
        sfn_result = sfn_two._addition(sfn_one.vals, sfn_one.nests)
        self.assertEqual(sfn_result.vals, [9, 1, 3, 5, 8, 8, 6, 6, 0, 8, 1, 8, 1])
        self.assertEqual(sfn_result.nests, [4, 4, 3, 2, 3, 5, 5, 5, 5, 3, 5, 5, 4])

    def test_explode(self):
        # self.assertEqual(explode(self.explode_case_one), [[[[0, 9], 2], 3], 4])
        sfn_one = SnailFishNum(self.explode_case_one)
        sfn_one.explode()
        self.assertEqual(
            (sfn_one.vals, sfn_one.nests), ([0, 9, 2, 3, 4], [4, 4, 3, 2, 1])
        )
        sfn_two = SnailFishNum(self.explode_case_two)
        sfn_two.explode()
        self.assertEqual(
            (sfn_two.vals, sfn_two.nests), ([7, 6, 5, 7, 0], [1, 2, 3, 4, 4])
        )
        sfn_three = SnailFishNum(self.explode_case_three)
        sfn_three.explode()
        self.assertEqual(
            (sfn_three.vals, sfn_three.nests),
            ([6, 5, 7, 0, 3], [2, 3, 4, 4, 1]),
        )
        sfn_four = SnailFishNum(self.explode_case_four)
        sfn_four.explode()
        self.assertEqual(
            (sfn_four.vals, sfn_four.nests),
            ([3, 2, 8, 0, 9, 5, 4, 3, 2], [2, 3, 4, 4, 2, 3, 4, 5, 5]),
        )
        sfn_five = SnailFishNum("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        sfn_five.explode()
        self.assertEqual(sfn_five.vals, [3, 2, 8, 0, 9, 5, 7, 0])
        self.assertEqual(sfn_five.nests, [2, 3, 4, 4, 2, 3, 4, 4])

    def test_ingest(self):
        self.assertEqual(
            self.sfn._ingest("[[[[[9, 8], 1], 2], 3], 4]"),
            ([9, 8, 1, 2, 3, 4], [5, 5, 4, 3, 2, 1]),
        )
        self.assertEqual(
            self.sfn._ingest("[[[9,1],3],5]"), ([9, 1, 3, 5], [3, 3, 2, 1])
        )
        self.assertEqual(
            self.sfn._ingest(self.explode_case_two),
            ([7, 6, 5, 4, 3, 2], [1, 2, 3, 4, 5, 5]),
        )
        self.assertEqual(
            self.sfn._ingest(self.explode_case_three),
            ([6, 5, 4, 3, 2, 1], [2, 3, 4, 5, 5, 1]),
        )
        self.assertEqual(
            self.sfn._ingest(self.explode_case_four),
            ([3, 2, 1, 7, 3, 6, 5, 4, 3, 2], [2, 3, 4, 5, 5, 2, 3, 4, 5, 5]),
        )

    def test_split(self):
        self.sfn.vals = [0, 7, 4, 15, 0, 13, 1, 1]
        self.sfn.nests = [4, 4, 3, 3, 4, 4, 2, 2]
        self.sfn.split()
        self.assertEqual(
            (self.sfn.vals, self.sfn.nests),
            ([0, 7, 4, 7, 8, 0, 13, 1, 1], [4, 4, 3, 4, 4, 4, 4, 2, 2]),
        )

    def test_reduce(self):
        sfn = SnailFishNum("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
        sfn.redu()
        self.assertEqual(
            (sfn.vals, sfn.nests),
            ([0, 7, 4, 7, 8, 6, 0, 8, 1], [4, 4, 3, 4, 4, 4, 4, 2, 2]),
        )


# ()

# [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
