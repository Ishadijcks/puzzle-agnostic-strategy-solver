from puzzles.raatsel.AbstractRaatsel import AbstractRaatsel


class Raatsel2x2(AbstractRaatsel):

    def from_hash(self, hash_string):
        both = hash_string.split(",")
        words = both[:self.get_word_cell_count()]
        categories = both[self.get_word_cell_count()::]

        raatsel = Raatsel2x2(self.available_words, self.available_categories, self.available_edges, self.matrix)

        for i in range(0, len(words)):
            word = words[i]
            if word != 'x':
                raatsel.word_candidates[i] = [int(word)]

        for i in range(0, len(categories)):
            category = categories[i]
            if category != 'x':
                raatsel.category_candidates[i] = [int(category)]

        return raatsel

    def __init__(self, words, categories, edges, matrix):
        super().__init__(2, words, categories, edges, matrix)

    def get_neighbours_for_cell(self, word):
        return [
            [1, 17],  # W0
            [0, 2, 18],  # W1
            [1, 3, 18],  # W2
            [2, 4],  # W3
            [3, 5, 19],  # W4
            [4, 6, 19],  # W5
            [5, 7],  # W6
            [6, 8, 20],  # W7
            [7, 9, 20],  # W8
            [8, 10],  # W9
            [9, 11, 21],  # W10
            [10, 12, 21],  # W11
            [11, 13],  # W12
            [12, 14, 22],  # W13
            [13, 15, 22],  # W14
            [14, 16],  # W15
            [15, 17, 23],  # W16
            [16, 0, 23],  # W17
            [1, 2, 24, 25],  # W18
            [4, 5, 25, 26],  # W19
            [7, 8, 26, 27],  # W20
            [10, 11, 27, 28],  # W21
            [13, 14, 28, 29],  # W22
            [16, 17, 29, 24],  # W23
            [25, 29, 23, 18],  # W24
            [24, 26, 18, 19],  # W25
            [25, 27, 19, 20],  # W26
            [26, 28, 20, 21],  # W27
            [29, 27, 21, 22],  # W28
            [24, 28, 22, 23],  # W29
        ][word]

    def get_edges_for_cell(self, cell):
        return [
            [5, 0],  # W0
            [0],  # W1
            [0],  # W2
            [0, 1],  # W3
            [1],  # W4
            [1],  # W5
            [1, 2],  # W6
            [2],  # W7
            [2],  # W8
            [2, 3],  # W9
            [3],  # W10
            [3],  # W11
            [3, 4],  # W12
            [4],  # W13
            [4],  # W14
            [4, 5],  # W15
            [5],  # W16
            [5],  # W17
            [],  # W18
            [],  # W19
            [],  # W20
            [],  # W21
            [],  # W22
            [],  # W23
            [],  # W24
            [],  # W25
            [],  # W26
            [],  # W27
            [],  # W28
            [],  # W29
        ][cell]

    def get_cells_for_edge(self, edge):
        return [
            [0, 1, 2, 3],
            [3, 4, 5, 6],
            [6, 7, 8, 9],
            [9, 10, 11, 12],
            [12, 13, 14, 15],
            [15, 16, 17, 0],
        ][edge]

    def get_categories_for_cell(self, word):
        return [
            [0],  # W0
            [0],  # W1
            [1],  # W2
            [1],  # W3
            [1],  # W4
            [2],  # W5
            [2],  # W6
            [2],  # W7
            [3],  # W8
            [3],  # W9
            [3],  # W10
            [4],  # W11
            [4],  # W12
            [4],  # W13
            [5],  # W14
            [5],  # W15
            [5],  # W16
            [0],  # W17
            [0, 1],  # W18
            [1, 2],  # W19
            [2, 3],  # W20
            [3, 4],  # W21
            [4, 5],  # W22
            [5, 0],  # W23
            [6, 0],  # W24
            [6, 1],  # W25
            [6, 2],  # W26
            [6, 3],  # W27
            [6, 4],  # W28
            [6, 5],  # W29
        ][word]

    def get_words_for_category(self, category):
        return [
            [0, 1, 18, 24, 23, 17],
            [2, 3, 4, 19, 25, 18],
            [19, 5, 6, 7, 20, 26],
            [27, 20, 8, 9, 10, 21],
            [22, 28, 21, 11, 12, 13],
            [16, 23, 29, 22, 14, 15],
            [24, 25, 26, 27, 28, 29],
        ][category]
