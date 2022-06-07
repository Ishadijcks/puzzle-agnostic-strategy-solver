from abc import ABC, abstractmethod


class AbstractPuzzle(ABC):
    def __init__(self):
        self.iteration = 0

    def solve(self, strategies, debug=False):
        while True:
            has_done_anything = self.solve_step(strategies)
            if debug:
                self.print_state()
            if self.is_impossible():
                if debug:
                    print("Solving was impossible")
                return False
            if not has_done_anything:
                if debug:
                    print("Nothing changed this iteration...")
                return False
            if self.is_solved():
                return True

    def solve_step(self, strategies):
        self.iteration += 1
        removals = []

        for strategy in strategies:
            removals += strategy.apply(self)

        numbers_placed = self.remove_removals(removals)

        return numbers_placed or len(removals) > 0

    @abstractmethod
    def is_solved(self) -> bool:
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def print_state(self) -> bool:
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def get_hash(self) -> str:
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def remove_removals(self, removals):
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def from_hash(self, hash_string):
        raise NotImplementedError("Please Implement this method")

    @abstractmethod
    def is_impossible(self):
        raise NotImplementedError("Please Implement this method")

