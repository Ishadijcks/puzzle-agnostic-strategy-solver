from puzzles.AbstractStrategy import AbstractStrategy


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
        has_done_anything = False

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
                has_done_anything = True
                for candidate_to_remove in candidates_to_remove:
                    raatsel.category_candidates[category].remove(candidate_to_remove)

        return has_done_anything
