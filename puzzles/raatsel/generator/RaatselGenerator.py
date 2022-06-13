import os
import random
import subprocess

from puzzles.raatsel.AbstractRaatsel import AbstractRaatsel
from puzzles.raatsel.Raatsel1x1 import Raatsel1x1
from puzzles.raatsel.Raatsel2x2 import Raatsel2x2
from puzzles.raatsel.RaatselSize import RaatselSize
from puzzles.raatsel.generator.DummyRaatsel2x2 import DummyRaatsel2x2


class RaatselGenerator:

    @staticmethod
    def generate_m(false_friends_desired, strategies):
        raatsel = DummyRaatsel2x2()

        possibilities = []

        for y in range(len(raatsel.matrix)):
            for x in range(len(raatsel.matrix[0])):
                if raatsel.matrix[y][x] != 1:
                    possibilities.append((x, y))
        random.shuffle(possibilities)
        max_possibilities = len(possibilities)

        false_friends = 0
        while false_friends < false_friends_desired and len(possibilities) > max_possibilities * 0.8:
            # print(false_friends, false_friends_desired, len(possibilities))
            (x, y) = possibilities.pop(0)

            copy = RaatselGenerator.copy(raatsel)
            copy.matrix[y][x] = 1
            copy.solve(strategies)
            if copy.is_solved():
                false_friends += 1
                raatsel.matrix[y][x] = 1

        return raatsel

    @staticmethod
    def copy(raatsel):
        return Raatsel2x2(raatsel.available_words, raatsel.available_categories, raatsel.available_edges,
                          raatsel.matrix)

    @staticmethod
    def generate_from_wordgraph(word_graph, size) -> AbstractRaatsel:
        file_name = 'temp.txt'
        word_graph.write_glasgow_to_file(file_name)
        return RaatselGenerator.generate_from_file(word_graph, os.path.join('cache', file_name), size)

    @staticmethod
    def generate_from_file(word_graph, target_file, strategies, size=RaatselSize.TwoByTwo) -> AbstractRaatsel:

        raatsel = None
        database_graph = RaatselGenerator.generate_m(10, strategies)

        while True:
            print("starting mapping...")
            # database_graph = DummyRaatsel2x2()

            database_graph.write_glasgow_to_file('database.txt')
            pattern_file = os.path.join('cache', 'database.txt')

            process = subprocess.Popen(
                ['./bin/glasgow_subgraph_solver', '--timeout', '30',
                 pattern_file, target_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, text=True)
            process.wait()
            stdout, stderr = process.communicate()
            if stderr:
                print("failed", stderr)
            # assert not stderr
            solutions = RaatselGenerator.parse_multiple_solutions(stdout, size)
            for words, categories, edges in solutions:

                matrix = word_graph.to_matrix(words, categories, edges)

                if size == RaatselSize.OneByOne:
                    raatsel = Raatsel1x1(words, categories, edges, matrix)
                else:
                    raatsel = Raatsel2x2(words, categories, edges, matrix)

                raatsel.solve(strategies)

                if raatsel.is_solved():
                    print("Successfully generated raatsel!", raatsel)
                    exit(0)
                    break
                else:
                    print("solving failed")

        print("Successfully generated raatsel!", raatsel)
        return raatsel

    @staticmethod
    def parse_solutions(solutions_string, size):
        output = solutions_string.split("\n")
        result = None
        for line in output:
            if line.startswith('mapping'):
                result = line
                break
        if result is None:
            print(solutions_string)
            raise Exception("No solution found")
        print(result)
        return RaatselGenerator.parse_mapping(result)

    @staticmethod
    def parse_multiple_solutions(solutions_string, size):
        output = solutions_string.split("\n")
        results = []
        for line in output:
            if line.startswith('mapping'):
                results.append(RaatselGenerator.parse_mapping(line))
        return results

    @staticmethod
    def parse_mapping(mapping):
        result = mapping.replace(") (", "|").replace("mapping = (", "").replace(")", "").replace(" ", "")
        mapping = result.split("|")

        words = [None] * 30
        categories = [None] * 7
        edges = [None] * 6

        try:
            for entry in mapping:
                split = entry.split("->")

                index = int(split[0][1:])
                if 'W' in split[0]:
                    words[index] = split[1]
                if 'C' in split[0]:
                    categories[index] = split[1]
                if 'E' in split[0]:
                    edges[index] = split[1]
            return words, categories, edges
        except:
            return words, categories, edges
