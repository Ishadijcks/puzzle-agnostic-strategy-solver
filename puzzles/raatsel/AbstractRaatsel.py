from abc import abstractmethod
import numpy as np
from tabulate import tabulate

from puzzles.AbstractPuzzle import AbstractPuzzle


class AbstractRaatsel(AbstractPuzzle):
    def __init__(self, size, words, categories, edges, matrix):
        super().__init__()
        self.size = size
        self.available_words = words
        self.available_categories = categories
        self.available_edges = edges
        self.matrix = matrix

        assert len(self.available_words) == self.get_word_cell_count()
        assert len(self.available_categories) == self.get_category_count()
        assert len(self.available_edges) == self.get_edge_count()

        self.word_candidates = []
        for i in range(0, len(self.available_words)):
            self.word_candidates.append(list(range(0, len(self.available_words))))

        self.category_candidates = []
        for i in range(0, len(self.available_categories)):
            self.category_candidates.append(list(range(0, len(self.available_categories))))

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
        pass

    def remove_removals(self, removals):
        for removal in removals:
            if removal.x == "cell":
                for candidate in removal.candidates:
                    self.word_candidates[removal.y].remove(candidate)
            if removal.x == "category":
                for candidate in removal.candidates:
                    self.category_candidates[removal.y].remove(candidate)

    def from_hash(self, hash_string):
        pass

    def __str__(self):
        return "Raatsel\n" \
               "Words: " + ', '.join(self.available_words) + "\n" + \
               "Edges: " + ', '.join(self.available_edges) + "\n" + \
               "Categories: " + ', '.join(self.available_categories) + "\n" + \
               "Matrix: \n" + tabulate(np.c_[self.available_words, self.matrix],
                                       headers=[""] + self.available_edges + self.available_categories) \
               + "\n"
