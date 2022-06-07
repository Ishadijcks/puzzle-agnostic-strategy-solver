import os.path

from nltk.corpus import wordnet as wn

from puzzles.raatsel.generator.WordGraph import WordGraph


class Wordnet(object):
    @staticmethod
    def hypo(s):
        return s.hyponyms()

    @staticmethod
    def hyper(s):
        return s.hypernyms()

    def __init__(self, blacklisted_categories=None) -> None:
        if blacklisted_categories is None:
            blacklisted_categories = []
        self.blacklisted_categories = blacklisted_categories

    def get_all_categories_for_synset(self, synset, max_parent=None):
        categories = []
        parents = [synset]
        while parents:
            pivot = parents.pop(0)
            if pivot == max_parent:
                categories.append(pivot)
                continue
            if pivot in categories:
                continue
            if self.normalize(pivot) in self.blacklisted_categories:
                continue
            categories.append(pivot)
            new_parents = pivot.hypernyms()
            for new_parent in new_parents:
                if new_parent not in parents:
                    parents.append(new_parent)
        # Remove first element which is the original synset
        if len(categories) > 0:
            categories.pop(0)
        return categories

    def get_all_instances(self, word):
        results = []
        queue = wn.synsets(word)
        while queue:
            pivot = queue.pop(0)
            children = pivot.hyponyms()
            for child in children:
                if child.hyponyms():
                    queue.append(child)
                else:
                    results.append(child)
        return results

    def format_synsets(self, synsets):
        res = []
        for synset in synsets:
            res.append(self.normalize(synset))
        return res

    def normalize(self, synset):
        return synset.lemmas()[0].name()

    def generate_word_graph(self, base_synset, max_depth, depth=0, word_graph=WordGraph()) -> WordGraph:
        if depth >= max_depth:
            return word_graph

        instances = self.get_all_instances(self.normalize(base_synset))

        print(instances)
        for synset in instances:
            word = self.normalize(synset)
            categories = self.get_all_categories_for_synset(synset, base_synset)
            formatted_categories = self.format_synsets(categories)
            word_graph.add_edges(word, formatted_categories)

            for i in range(min(5, len(categories))):
                self.generate_word_graph(categories[i], max_depth, depth+1, word_graph)
            print(word, categories)

        return word_graph
