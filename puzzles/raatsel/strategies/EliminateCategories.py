from puzzles.AbstractStrategy import AbstractStrategy
from solver.RemoveCandidate import RemoveCandidate


class EliminateCategories(AbstractStrategy):
    """Iterate over all category options and eliminate if wouldn't fit"""

    @staticmethod
    def get_name():
        return "Eliminate Categories"

    @staticmethod
    def get_difficulty():
        return 100

    @staticmethod
    def apply(raatsel):
        removals = []

        for category in range(0, len(raatsel.category_candidates)):
            candidates = raatsel.category_candidates[category]
            if len(candidates) == 1:
                continue
            surrounding_words = raatsel.get_words_for_category(category)

            placed_words = list(filter(lambda w: len(raatsel.word_candidates[w]) == 1, surrounding_words))

            candidates_to_remove = set([])

            for candidate in candidates:
                for placed_word in placed_words:
                    if not raatsel.matrix_category(placed_word, candidate):
                        candidates_to_remove.add(candidate)
                        continue

            if len(candidates_to_remove) > 0:
                removals.append(
                    RemoveCandidate("category", category, candidates_to_remove, EliminateCategories.get_name(),
                                    EliminateCategories.get_difficulty())
                )

        return removals
