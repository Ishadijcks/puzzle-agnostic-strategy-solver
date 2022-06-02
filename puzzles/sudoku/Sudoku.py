import numpy as np
from tabulate import tabulate

from puzzles.AbstractPuzzle import AbstractPuzzle
from solver.NumberPlaced import NumberPlaced


class Sudoku(AbstractPuzzle):

    def from_hash(self, hash_string):
        return Sudoku(hash_string)

    def __init__(self, clues):
        super().__init__()
        self.solved_grid = np.ndarray((9, 9))
        self.grid_candidates = np.ndarray((9, 9), dtype='object')

        for y in range(0, 9):
            for x in range(0, 9):
                i = 9 * y + x
                # print(i)
                clue = int(clues[i])
                if clue != 0:
                    self.grid_candidates[y, x] = [clue]
                    self.solved_grid[y, x] = clue
                else:
                    self.grid_candidates[y, x] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    self.solved_grid[y, x] = 0

    def is_solved(self):
        for y in range(0, 9):
            for x in range(0, 9):
                if len(self.grid_candidates[y, x]) > 1:
                    return False
        return True

    def remove_removals(self, removals):
        numbers_placed = []
        for removal in removals:
            for candidate in removal.candidates:
                if candidate in self.grid_candidates[removal.y, removal.x]:
                    self.grid_candidates[removal.y, removal.x].remove(candidate)
                    if len(self.grid_candidates[removal.y, removal.x]) == 0:
                        self.print_state()
                        raise Exception(f"Empty domain at ({removal.x}, {removal.y}) after {removal})")
                    if len(self.grid_candidates[removal.y, removal.x]) == 1 and \
                            self.solved_grid[removal.y, removal.x] == 0:
                        placed_value = self.grid_candidates[removal.y, removal.x][0]
                        self.solved_grid[removal.y, removal.x] = placed_value
                        # print(f"placed number {placed_value} on ({removal.y}, {removal.x} with {removal.strategy})")
                        numbers_placed.append(
                            NumberPlaced(9 * removal.y + removal.x, placed_value, removal.strategy, removal.difficulty))
        return numbers_placed

    def get_related_cells(self, x, y):
        return np.concatenate((
            self.get_row(y).flatten(),
            self.get_col(x).flatten(),
            self.get_group(x, y).flatten(),
        ))

    def get_row(self, index):
        return self.grid_candidates[index, :]

    def get_col(self, index):
        return self.grid_candidates[:, index]

    def get_group(self, x, y):
        index_x = x // 3
        index_y = y // 3
        return self.grid_candidates[3 * index_y: 3 * index_y + 3, 3 * index_x: 3 * index_x + 3]

    def get_hash(self):
        res = ""
        for y in range(0, 9):
            for x in range(0, 9):
                res += str(int(self.solved_grid[y, x]))
        return res

    @staticmethod
    def get_state_transitions(current_hash, next_hash):
        assert len(current_hash) == len(next_hash)
        res = []
        for i in range(0, len(current_hash)):
            if current_hash[i] != next_hash[i]:
                possible_state = list(current_hash)
                possible_state[i] = next_hash[i]
                possible_state = ''.join(possible_state)
                res.append(possible_state)

        return res

    def print_state(self):
        print(tabulate(self.grid_candidates))
        print(tabulate(self.solved_grid))
        print("Solved:", self.is_solved())
