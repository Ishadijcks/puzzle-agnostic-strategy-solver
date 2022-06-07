import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os.path


class WordGraph:

    def __init__(self, words=None, categories=None):
        if words is None:
            words = []
        if categories is None:
            categories = []
        self.words = words
        self.categories = categories

        self.edges = []

    def get_combined(self):
        return self.words + self.categories

    def add_edge(self, source, target):
        if source not in self.words:
            self.words.append(source)
        if target not in self.categories:
            self.categories.append(target)
        self.edges.append((source, target))

    def has_edge(self, source, target):
        return (source, target) in self.edges

    def add_edges(self, source, targets):
        for target in targets:
            if not self.has_edge(source, target):
                self.add_edge(source, target)

    def get_pandas_dataframe(self):
        from_list = []
        to_list = []
        for edge in self.edges:
            from_list.append(edge[0])
            to_list.append(edge[1])
        return {
            'from': from_list,
            'to': to_list
        }

    def plot(self):
        data_frame = self.get_pandas_dataframe()
        df = pd.DataFrame(data_frame)

        G = nx.from_pandas_edgelist(df, 'from', 'to')

        nx.draw(G, with_labels=True, pos=nx.shell_layout(G))
        plt.show()

    def _get_edges_out_of_word(self, word):
        res = []
        for edge in self.edges:
            if edge[0] == word:
                res.append(edge)
        return res

    def to_matrix(self, words, categories, edges):
        matrix = []
        for word in words:
            combined = edges + categories
            row = []
            for entry in combined:
                row.append(1 if self.has_edge(word, entry) else 0)
            matrix.append(row)
        return matrix

    def to_glasgow(self):
        res = ""
        for edge in self.edges:
            word = edge[0]
            category = edge[1]
            res += word + ">" + category + '\n'
        return res

    @staticmethod
    def from_glasgow_file(file_name):
        with open(os.path.join('cache', file_name)) as f:
            lines = f.readlines()
        word_graph = WordGraph()
        for line in lines:
            line = line.replace('\n', '')
            splits = line.split(">")
            source = splits[0]
            target = splits[1]
            word_graph.add_edge(source, target)

        f.close()
        return word_graph

    def write_glasgow_to_file(self, file_name) -> None:
        f = open(os.path.join('cache', file_name), "w")
        f.write(self.to_glasgow())
        f.close()

    def print(self):
        print(self.to_glasgow())
