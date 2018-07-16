

import nltk
from nltk import word_tokenize, pos_tag


class PennTreebank:

    nltk.download('averaged_perceptron_tagger', quiet=True)

    @staticmethod
    def get_pos(sentence):
        return pos_tag(word_tokenize(sentence))

    @staticmethod
    def get_pos_tag(pos):
        if 'NN' in pos:
            return 'n'
        elif 'VB' in pos:
            return 'v'
        elif 'JJ' in pos:
            return 'a'
        elif 'RB' in pos:
            return 'r'
