from puzzles.AbstractStrategy import AbstractStrategy


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
        has_done_anything = False

        # Words
        already_placed_words = []
        for cell_index in range(0, raatsel.get_word_cell_count()):
            if len(raatsel.word_candidates[cell_index]) == 1:
                already_placed_words.append(raatsel.word_candidates[cell_index][0])

        for placed in already_placed_words:
            for cell_index in range(0, raatsel.get_word_cell_count()):
                if len(raatsel.word_candidates[cell_index]) > 1 and placed in raatsel.word_candidates[cell_index]:
                    raatsel.word_candidates[cell_index].remove(placed)
                    has_done_anything = True

        # Categories
        already_placed_categories = []
        for category_index in range(0, raatsel.get_category_count()):
            if len(raatsel.category_candidates[category_index]) == 1:
                already_placed_categories.append(raatsel.category_candidates[category_index][0])

        for placed in already_placed_categories:
            for category_index in range(0, raatsel.get_category_count()):
                if len(raatsel.category_candidates[category_index]) > 1 and placed in raatsel.category_candidates[category_index]:
                    raatsel.category_candidates[category_index].remove(placed)
                    has_done_anything = True
        return has_done_anything
