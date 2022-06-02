from puzzles.AbstractStrategy import AbstractStrategy
from solver.RemoveCandidate import RemoveCandidate


class HiddenSingle(AbstractStrategy):
    """Place values if there is only one place in the group for them to go"""

    @staticmethod
    def get_name():
        return "Hidden Single"

    @staticmethod
    def get_difficulty():
        return 100

    @staticmethod
    def apply(sudoku):

        removals = []
        # Rows
        for i in range(0, 9):
            col = sudoku.get_row(i)

            # Remove already placed numbers
            available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for options in col:
                if len(options) == 1:
                    available_numbers.remove(options[0])

            for number in available_numbers:
                appears_in = []
                for index, options in enumerate(col):
                    if number in options:
                        appears_in.append(index)
                # Now we know it must be placed here
                if len(appears_in) == 1:
                    # print("row", i, "number", number, "appears in", appears_in)
                    remove_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    remove_all.remove(number)
                    removals.append(
                        RemoveCandidate(
                            appears_in[0],
                            i,
                            remove_all,
                            HiddenSingle.get_name(),
                            HiddenSingle.get_difficulty()
                        )
                    )

        # Columns
        for i in range(0, 9):
            col = sudoku.get_col(i)

            # Remove already placed numbers
            available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for options in col:
                if len(options) == 1:
                    available_numbers.remove(options[0])

            for number in available_numbers:
                appears_in = []
                for index, options in enumerate(col):
                    if number in options:
                        appears_in.append(index)
                # Now we know it must be placed here
                if len(appears_in) == 1:
                    # print("col", i, "number", number, "appears in", appears_in)
                    remove_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    remove_all.remove(number)
                    removals.append(
                        RemoveCandidate(
                            i,
                            appears_in[0],
                            remove_all,
                            HiddenSingle.get_name(),
                            HiddenSingle.get_difficulty()
                        )
                    )

        # Groups
        for i in range(0, 9):
            top_left_x = (i % 3) * 3
            top_left_y = (i // 3) * 3

            group = sudoku.get_group(top_left_x, top_left_y).flatten()

            # Remove already placed numbers
            available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for options in group:
                if len(options) == 1:
                    available_numbers.remove(options[0])

            for number in available_numbers:
                appears_in = []
                for index, options in enumerate(group):
                    if number in options:
                        appears_in.append(index)
                # Now we know it must be placed here
                if len(appears_in) == 1:
                    # print("group", i, "number", number, "appears in", appears_in)
                    local_index = appears_in[0]
                    x = top_left_x + local_index % 3
                    y = top_left_y + local_index // 3
                    remove_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    remove_all.remove(number)
                    removals.append(
                        RemoveCandidate(
                            x,
                            y,
                            remove_all,
                            HiddenSingle.get_name(),
                            HiddenSingle.get_difficulty()
                        )
                    )

        return removals
