from puzzles.AbstractStrategy import AbstractStrategy
from solver.RemoveCandidate import RemoveCandidate


class NakedSingle(AbstractStrategy):
    """Place numbers if cells can only have one possible value"""

    @staticmethod
    def get_name():
        return "Naked Single"

    @staticmethod
    def get_difficulty():
        return 50

    @staticmethod
    def apply(sudoku):

        removals = []
        for y in range(0, 9):
            for x in range(0, 9):
                cell = sudoku.grid_candidates[y, x]
                if len(cell) == 1:
                    continue

                related = sudoku.get_related_cells(x, y)

                already_placed = set()

                for r in related:
                    if len(r) == 1 and r[0] in cell:
                        already_placed.add(r[0])
                if len(already_placed) > 0:
                    removals.append(
                        RemoveCandidate(x, y, list(already_placed), NakedSingle.get_name(), NakedSingle.get_difficulty()
                                        ))

        return removals
