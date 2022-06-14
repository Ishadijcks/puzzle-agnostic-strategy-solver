import os
from abc import abstractmethod
import numpy as np
from tabulate import tabulate

from puzzles.AbstractPuzzle import AbstractPuzzle
from solver.NumberPlaced import NumberPlaced


class AbstractRaatsel(AbstractPuzzle):
    def __init__(self, size, words, categories, edges, matrix):
        super().__init__()
        self.size = size
        self.available_words = words
        self.available_categories = categories
        self.available_edges = edges
        self.available_groups = edges + categories

        self.word_was_solved = []
        self.category_was_solved = []
        self.matrix = matrix

        assert len(self.available_words) == self.get_word_cell_count()
        assert len(self.available_categories) == self.get_category_count()
        assert len(self.available_edges) == self.get_edge_count()

        self.word_candidates = []
        for i in range(0, len(self.available_words)):
            self.word_candidates.append(list(range(0, len(self.available_words))))
            self.word_was_solved.append(False)

        self.category_candidates = []
        for i in range(0, len(self.available_categories)):
            self.category_candidates.append(list(range(0, len(self.available_categories))))
            self.category_was_solved.append(False)

    def print_state(self):
        print("==== WORDS ====")
        formatted_candidates = []
        for row in self.word_candidates:
            formatted_row = [self.available_words[x] for x in row]
            formatted_candidates.append(formatted_row)
        print(tabulate(formatted_candidates, showindex=range(self.get_word_cell_count()), tablefmt="plain"))
        print("==== CATEGORIES ====")
        formatted_candidates = []
        for row in self.category_candidates:
            formatted_row = [self.available_categories[x] for x in row]
            formatted_candidates.append(formatted_row)
        print(tabulate(formatted_candidates, showindex=range(self.get_category_count()), tablefmt="plain"))

        if self.is_solved():
            print("==== SOLVED!!! ====")

    def can_word_be_in_cell(self, word, cell):
        categories = self.get_categories_for_cell(cell)
        for category in categories:
            possible_categories = self.category_candidates[category]
            if len(possible_categories) == 1:
                # TODO currently it only eliminates if there is 1 category.
                if not self.matrix_category(word, possible_categories[0]):
                    return False
        edges = self.get_edges_for_cell(cell)
        for edge in edges:
            if not self.matrix_edge(word, edge):
                return False

        return True

    def is_solved(self):
        for candidates in self.category_candidates:
            if len(candidates) != 1:
                return False
        for candidates in self.word_candidates:
            if len(candidates) != 1:
                return False
        return True

    def matrix_edge(self, word, edge):
        return self.matrix[word][edge]

    def matrix_category(self, word, category):
        return self.matrix[word][self.get_edge_count() + category]

    @abstractmethod
    def get_neighbours_for_cell(self, word):
        pass

    @abstractmethod
    def get_edges_for_cell(self, cell):
        pass

    @abstractmethod
    def get_cells_for_edge(self, edge):
        pass

    @abstractmethod
    def get_categories_for_cell(self, word):
        pass

    @abstractmethod
    def get_words_for_category(self, category):
        pass

    def get_edge_count(self):
        """Always fixed to 6"""
        return 6

    def get_word_cell_count(self):
        """3n(3n-1)"""
        return 3 * self.size * (3 * self.size - 1)

    def get_category_count(self):
        """3n(n-1) + 1"""
        return 3 * self.size * (self.size - 1) + 1

    def get_hash(self) -> str:
        words = []
        for w in self.word_candidates:
            if len(w) == 1:
                words.append(w[0])
            else:
                words.append("x")
        word_hash = ','.join(words)

        categories = []
        for c in self.category_candidates:
            if len(c) == 1:
                categories.append(c[0])
            else:
                categories.append("x")
        category_hash = ','.join(categories)

        return word_hash + "," + category_hash

    def remove_removals(self, removals):
        numbers_placed = []
        for removal in removals:
            if removal.x == "word":
                for candidate in removal.candidates:
                    if candidate in self.word_candidates[removal.y]:

                        self.word_candidates[removal.y].remove(candidate)

                        # Now check if this is the first time there is only one candidate left, this means a placement
                        if len(self.word_candidates[removal.y]) == 1 and \
                                self.word_was_solved[removal.y] == False:
                            placed_value = self.word_candidates[removal.y][0]
                            self.word_was_solved[removal.y] = True
                            # print(f"placed number {placed_value} on ({removal.y}, {removal.x} with {removal.strategy})")

                            index = removal.y
                            numbers_placed.append(
                                NumberPlaced(index, placed_value, removal.strategy, removal.difficulty))

            if removal.x == "category":
                for candidate in removal.candidates:
                    if candidate in self.category_candidates[removal.y]:
                        self.category_candidates[removal.y].remove(candidate)

                        if len(self.category_candidates[removal.y]) == 1 and \
                                self.category_was_solved[removal.y] == False:
                            placed_value = self.category_candidates[removal.y][0]
                            self.category_was_solved[removal.y] = True

                            index = removal.y + self.get_word_cell_count()
                            numbers_placed.append(
                                NumberPlaced(index, placed_value, removal.strategy, removal.difficulty))

        return numbers_placed

    def to_glasgow(self):
        res = ""
        for y in range(0, len(self.matrix)):
            for x in range(0, len(self.matrix[0])):
                if self.matrix[y][x] == 1:
                    res += self.available_words[y] + ">" + self.available_groups[x] + '\n'
        return res

    def write_glasgow_to_file(self, file_name) -> None:
        f = open(os.path.join('cache', file_name), "w")
        f.write(self.to_glasgow())
        f.close()

    def is_impossible(self):
        for c in self.category_candidates:
            if len(c) == 0:
                return True
        for w in self.word_candidates:
            if len(w) == 0:
                return True
        return False

    def __str__(self):
        return "Raatsel\n" \
               "Words: " + ', '.join(self.available_words) + "\n" + \
               "Edges: " + ', '.join(self.available_edges) + "\n" + \
               "Categories: " + ', '.join(self.available_categories) + "\n" + \
               "Matrix: \n" + tabulate(np.c_[self.available_words, self.matrix],
                                       headers=[""] + self.available_edges + self.available_categories) \
               + "\n"
