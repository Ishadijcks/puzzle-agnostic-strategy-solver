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

    def __init__(self, blacklisted_categories=None, max_words=None, max_depth=None) -> None:
        if blacklisted_categories is None:
            blacklisted_categories = []
        if max_words is None:
            max_words = 100
        if max_depth is None:
            max_depth = 1

        self.max_words = max_words
        self.max_depth = max_depth
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

    def generate_word_graph(self, base_synset) -> WordGraph:
        word_graph = self._generate_word_graph(base_synset, 0, WordGraph())
        # Find closures to dense relations
        print("densing", len(word_graph.words))
        for i in range(0, len(word_graph.words)):
            for j in range(i, len(word_graph.words)):
                word1 = word_graph.words[i]
                word2 = word_graph.words[j]

                syn1 = wn.synsets(word1)[0]
                syn2 = wn.synsets(word2)[0]

                common = self.normalize(syn1.lowest_common_hypernyms(syn2)[0])
                if common not in self.blacklisted_categories:
                    word_graph.add_edge(word1, common)
                    word_graph.add_edge(word2, common)

        print("adding factuals")
        # Add factuals
        alphabet = ["Q", "X", "Y", "Z"]
        for word in word_graph.words:
            word_graph.add_edge(word, "starts-" + word[0].upper())
            word_graph.add_edge(word, "length-" + str(len(word.replace("-", "").replace("_", ""))))
            for letter in alphabet:
                if letter.upper() in word.upper():
                    word_graph.add_edge(word, "contains-" + letter)
        return word_graph

    def _generate_word_graph(self, base_synset, depth, word_graph) -> WordGraph:
        if depth >= self.max_depth or len(word_graph.words) > self.max_words:
            return word_graph

        instances = self.get_all_instances(self.normalize(base_synset))

        # print(instances)
        for synset in instances:
            word = self.normalize(synset)
            categories = self.get_all_categories_for_synset(synset, base_synset)
            formatted_categories = self.format_synsets(categories)
            word_graph.add_edges(word, formatted_categories)

            if len(word_graph.words) > self.max_words:
                return word_graph
            for i in range(min(5, len(categories))):
                self._generate_word_graph(categories[i], depth + 1, word_graph)
            print(word, categories)

        return word_graph
