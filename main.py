from puzzles.raatsel.RaatselSize import RaatselSize
from puzzles.raatsel.generator.RaatselGenerator import RaatselGenerator
from puzzles.raatsel.generator.WordGraph import WordGraph
from puzzles.raatsel.instances.SoloRaatsel import get_realistic_2x2_raatsel
from puzzles.raatsel.strategies.EliminateCategories import EliminateCategories
from puzzles.raatsel.strategies.EliminatePlacedElements import EliminatePlacedElements
from puzzles.raatsel.strategies.EliminateWords import EliminateWords
from puzzles.sudoku.instances.sudoku_easy_1 import get_easy1
from puzzles.sudoku.strategies.HiddenSingle import HiddenSingle
from puzzles.sudoku.strategies.NakedSingle import NakedSingle
from rater.Rater import Rater

raatsel_strategies = [EliminateCategories, EliminateWords, EliminatePlacedElements]


def solve_easy_sudoku():
    sudoku = get_easy1()
    sudoku.solve([HiddenSingle, NakedSingle], True)
    sudoku.print_state()


def solve_realistic_raatsel():
    raatsel = get_realistic_2x2_raatsel()
    raatsel.solve([
        EliminateCategories,
        EliminateWords,
        EliminatePlacedElements
    ])
    raatsel.print_state()
    print(raatsel.is_solved())


def rate_realistic_raatsel():
    raatsel = get_realistic_2x2_raatsel()
    rater = Rater(10)
    rater.time_expanded_rating(raatsel, [EliminateCategories, EliminateWords, EliminatePlacedElements])
    print(raatsel.is_solved())


def rate_easy_sudoku():
    sudoku = get_easy1()
    rater = Rater(10)
    rater.time_expanded_rating(sudoku, [HiddenSingle, NakedSingle])


def test_generate_m():
    results = []
    for f in range(0, 40):
        success = 0
        for i in range(1000):
            # print(i)
            raatsel = RaatselGenerator.generate_m(f, raatsel_strategies)
            if raatsel.solve(raatsel_strategies):
                success += 1
        results.append(success)
        print(results)
    print(results)


def main():
    raatsel = RaatselGenerator.generate_from_file(WordGraph.from_glasgow_file("pole.txt"), 'cache/pole.txt',
                                                  raatsel_strategies, RaatselSize.TwoByTwo)
    raatsel.solve(raatsel_strategies)
    print("Solvable?", raatsel.is_solved())


if __name__ == '__main__':
    main()
