from puzzles.raatsel.instances.SoloRaatsel import get_realistic_2x2_raatsel
from puzzles.raatsel.strategies.EliminateCategories import EliminateCategories
from puzzles.raatsel.strategies.EliminatePlacedElements import EliminatePlacedElements
from puzzles.raatsel.strategies.EliminateWords import EliminateWords
from puzzles.sudoku.instances.sudoku_easy_1 import get_easy1
from puzzles.sudoku.strategies.HiddenSingle import HiddenSingle
from puzzles.sudoku.strategies.NakedSingle import NakedSingle
from rater.Rater import Rater


def solve_easy_sudoku():
    sudoku = get_easy1()
    sudoku.solve([HiddenSingle, NakedSingle], True)
    sudoku.print_state()


def solve_realistic_raatsel():
    raatsel = get_realistic_2x2_raatsel()
    raatsel.solve([
        # EliminateCategories,
        EliminateWords,
        # EliminatePlacedElements
    ])
    raatsel.print_state()
    print(raatsel.is_solved())


def rate_easy_sudoku():
    sudoku = get_easy1()
    rater = Rater(10)
    rater.time_expanded_rating(sudoku, [HiddenSingle, NakedSingle])


def main():
    solve_realistic_raatsel()


if __name__ == '__main__':
    main()
