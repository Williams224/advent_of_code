import pandas as pd
import numpy as np


class BingoCard:
    def __init__(self, values):
        self.values = values
        self.marks = np.zeros((5, 5), dtype=bool)
        self.complete = False

    def mark_card(self, n):
        if self.complete:
            return None

        self.marks[np.where(self.values == n)] = True
        if self.check_card():
            score = self.calculate_score(n)
            print(f" Score is: {score}")
            self.complete = True
            return score

        return None

    def check_card(self):
        vertical_sums = np.sum(self.marks, axis=0)
        horizontal_sums = np.sum(self.marks, axis=1)
        return np.any(horizontal_sums == 5) or np.any(vertical_sums == 5)

    def calculate_score(self, n):
        board_sum = np.sum(self.values[~self.marks])
        return board_sum * n


def find_first_win_score(calls, cards):
    for call in calls:
        for bc in cards:
            winning_score = bc.mark_card(call)
            if winning_score:
                return winning_score


def find_last_win_score(calls, cards):
    for call in calls:
        for bc in cards:
            winning_score = bc.mark_card(call)
            if winning_score:
                print(winning_score)


if __name__ == "__main__":
    calls = np.array(pd.read_csv("day_four/input_calls.txt").T.index, dtype=int)
    cards_values = np.array_split(np.loadtxt("day_four/input.txt", dtype=int), 100)

    bingo_cards = [BingoCard(v) for v in cards_values]

    find_first_win_score(calls, bingo_cards)

    find_last_win_score(calls, bingo_cards)
