from puzzles.AbstractStrategy import AbstractStrategy
from solver.RemoveCandidate import RemoveCandidate


class EliminatePlacedElements(AbstractStrategy):
    """Remove categories and words from options if they are already assigned"""

    @staticmethod
    def get_name():
        return "Eliminate Placed"

    @staticmethod
    def get_difficulty():
        return 50

    @staticmethod
    def apply(raatsel):
        removals = []

        # Words
        already_placed_words = []
        for cell_index in range(0, raatsel.get_word_cell_count()):
            if len(raatsel.word_candidates[cell_index]) == 1:
                already_placed_words.append(raatsel.word_candidates[cell_index][0])

        for placed in already_placed_words:
            for cell_index in range(0, raatsel.get_word_cell_count()):
                if len(raatsel.word_candidates[cell_index]) > 1 and placed in raatsel.word_candidates[cell_index]:
                    removals.append(
                        RemoveCandidate(
                            "word", cell_index, [placed],
                            EliminatePlacedElements.get_name(),
                            EliminatePlacedElements.get_difficulty()
                        )
                    )

        # Categories
        already_placed_categories = []
        for category_index in range(0, raatsel.get_category_count()):
            if len(raatsel.category_candidates[category_index]) == 1:
                already_placed_categories.append(raatsel.category_candidates[category_index][0])

        for placed in already_placed_categories:
            for category_index in range(0, raatsel.get_category_count()):
                if len(raatsel.category_candidates[category_index]) > 1 and placed in raatsel.category_candidates[
                    category_index]:
                    removals.append(
                        RemoveCandidate(
                            "category", category_index, [placed],
                            EliminatePlacedElements.get_name(),
                            EliminatePlacedElements.get_difficulty()
                        )
                    )

        return removals
