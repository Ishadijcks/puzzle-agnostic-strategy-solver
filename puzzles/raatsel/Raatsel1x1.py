from puzzles.raatsel.AbstractRaatsel import AbstractRaatsel


class Raatsel1x1(AbstractRaatsel):
    def __init__(self, words, categories, edges, matrix):
        super().__init__(1, words, categories, edges, matrix)

    def get_neighbours_for_cell(self, word):
        return [
            [5, 1],
            [0, 2],
            [1, 3],
            [2, 4],
            [3, 5],
            [4, 0],
        ][word]

    def get_edges_for_cell(self, cell):
        return [
            [5, 0],
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
        ][cell]

    def get_cells_for_edge(self, edge):
        return [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 0],
        ][edge]

    def get_categories_for_cell(self, word):
        return [0]

    def get_words_for_category(self, category):
        if category == 0:
            return [0, 1, 2, 3, 4, 5]
