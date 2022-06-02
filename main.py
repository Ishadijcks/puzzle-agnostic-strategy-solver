from puzzles.sudoku.instances.sudoku_easy_1 import get_easy1
from puzzles.sudoku.strategies.HiddenSingle import HiddenSingle
from puzzles.sudoku.strategies.NakedSingle import NakedSingle
from rater.Rater import Rater


def solve_easy_sudoku():
    sudoku = get_easy1()
    sudoku.solve([HiddenSingle, NakedSingle], True)
    sudoku.print_state()

def rate_easy_sudoku():
    sudoku = get_easy1()
    rater = Rater(10)
    rater.time_expanded_rating(sudoku, [HiddenSingle, NakedSingle])


def main():
    rate_easy_sudoku()

if __name__ == '__main__':
    main()
