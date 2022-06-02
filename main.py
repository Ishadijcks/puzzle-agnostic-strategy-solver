from puzzles.raatsel.instances.sudoku_easy_1 import get_easy1
from puzzles.sudoku.strategies.HiddenSingle import HiddenSingle
from puzzles.sudoku.strategies.NakedSingle import NakedSingle


def solve_easy_sudoku():
    sudoku = get_easy1()
    sudoku.solve([HiddenSingle, NakedSingle], True)
    sudoku.print_state()


def main():
    sudoku = get_easy1()
    sudoku.solve([HiddenSingle, NakedSingle], True)
    sudoku.print_state()


if __name__ == '__main__':
    main()
