from itertools import cycle, product
import numpy as np
import copy

ROLL_THREE_DICE_OUTCOMES = list(
    map(lambda x: x[0] + x[1] + x[2], list(product([1, 2, 3], [1, 2, 3], [1, 2, 3])))
)


class Die:
    def __init__(self):
        self.n_rolls = 0

    def roll(self):
        self.n_rolls += 1


class DeterministicDie(Die):
    def __init__(self, sides):
        super().__init__()
        self.sides = sides
        self.cyclic_iterator = cycle([i for i in range(1, sides + 1)])

    def roll(self):
        super().roll()
        return next(self.cyclic_iterator)


class Player:
    def __init__(self, start_pos, winning_score=1000):
        self.starting_pos = start_pos
        self.current_pos = start_pos
        self.winning_score = winning_score
        self.score = 0
        self.position_iterator = cycle([i for i in range(1, 11)])
        print("init")
        n_moves_start = self.starting_pos
        for _ in range(0, n_moves_start):
            self.current_pos = next(self.position_iterator)

    def take_turn(self, die=None, moves=None):
        if die != None:
            moves = np.sum([die.roll(), die.roll(), die.roll()])
        print(f"moving {moves} positions")
        for _ in range(0, moves):
            self.current_pos = next(self.position_iterator)

        self.score += self.current_pos

        if self.score >= self.winning_score:
            return True

        return False


def gen_play(player_one, player_two, moves):
    if moves > 0:
        if player_one.take_turn(moves=moves):
            return 1
        if player_two.take_turn(moves=moves):
            return 0
    res = 0

    for i in ROLL_THREE_DICE_OUTCOMES:
        res += gen_play(copy.deepcopy(player_one), copy.deepcopy(player_two), i)

    return res


if __name__ == "__main__":

    # dd = DeterministicDie(100)

    # p1 = Player(5)

    # p2 = Player(10)

    # for i in range(0, 1000):
    #    if p1.take_turn(dd):
    #        print("p1 wins! ")
    #        break
    #    if p2.take_turn(dd):
    #        print("p2 wins! ")
    #        break

    p_part_two_one = Player(4, winning_score=21)

    p_part_two_two = Player(8, winning_score=21)

    print(gen_play(p_part_two_one, p_part_two_two, 0))

    print("h")

    # 1 universe
    # p1 take turn first roll generates 3 universes, each one a different result.  in each of three universes roll again, generate 3 and roll again,
    # p1 plays all of 9 different values 1 + 1 + 1, 2 + 1 +1 etc.
    # p2 take turn and generates 9 universes, each one a different result, iterate accordingly
    # in each of 9 universes roll dice and

    # 1 universe
    # player take turn and generate 27 universes with player copies and in each take a turn
    # for each of the now created universes
