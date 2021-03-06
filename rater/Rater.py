from puzzles.AbstractPuzzle import AbstractPuzzle


class Rater:
    def __init__(self, max_runtime):
        self.max_runtime = max_runtime

    def time_expanded_rating(self, puzzle: AbstractPuzzle, strategies):
        starting_hash = puzzle.get_hash()
        print(starting_hash)
        time_left = starting_hash.count("x")
        print(f"Starting rating with {time_left} steps")

        amount_over_time = []
        hashes_over_time = [
            [starting_hash]
        ]
        for i in range(0, time_left + 1):
            current_hashes = hashes_over_time[i]
            if i > 1:
                hashes_over_time[i-1] = None

            amount_over_time.append(len(current_hashes))
            print(len(current_hashes), "hashes at timestep", i)
            print("hashes over time", amount_over_time)

            new_hashes = set()
            for current_hash in current_hashes:
                assert current_hash.count("x") == time_left - i
                puzzle = puzzle.from_hash(current_hash)
                numbers_placed = puzzle.solve_step(strategies)
                while isinstance(numbers_placed, bool):
                    if not numbers_placed:
                        numbers_placed = []
                    else:
                        numbers_placed = puzzle.solve_step(strategies)
                if not numbers_placed:
                    continue
                next_hashes = self.get_next_hashes(current_hash, numbers_placed)

                for next_hash in next_hashes:
                    new_hashes.add(next_hash)
            hashes_over_time.append(new_hashes)

    @staticmethod
    def get_next_hashes(previous_hash, placed_numbers):
        res = []
        for placed_number in placed_numbers:
            hash_list = previous_hash.split(",")
            hash_list[placed_number.index] = str(placed_number.value)
            res.append(','.join(hash_list))
        return res
