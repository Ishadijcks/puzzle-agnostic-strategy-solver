from puzzles.AbstractStrategy import AbstractStrategy
from solver.RemoveCandidate import RemoveCandidate


class EliminateWords(AbstractStrategy):
    """Iterate over all word candidates for each cell.
    Eliminate candidates if they don't fit with the categories and edges"""

    @staticmethod
    def get_name():
        return "Eliminate Words"

    @staticmethod
    def get_difficulty():
        return 50

    @staticmethod
    def apply(raatsel):
        removals = []
        for cell_index in range(0, raatsel.get_word_cell_count()):
            candidates = raatsel.word_candidates[cell_index]

            candidates_to_remove = []
            for word_candidate in candidates:
                if not raatsel.can_word_be_in_cell(word_candidate, cell_index):
                    candidates_to_remove.append(word_candidate)

            if candidates_to_remove:
                removals.append(
                    RemoveCandidate("word", cell_index, candidates_to_remove, EliminateWords.get_name(),
                                    EliminateWords.get_difficulty())
                )

            if AbstractStrategy.debug:
                print("Cell", cell_index, "Removing candidates", candidates_to_remove)

        return removals
