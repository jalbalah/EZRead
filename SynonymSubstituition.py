

from difflib import SequenceMatcher
from termcolor import cprint
from pdb import set_trace as st

from WordNet import WordNet
from PennTreebank import PennTreebank
from ColorOutput import ColorOutput


class SynonymSubstituition:

    similarity = .8
    num_syns = 4

    def __new__(cls, *args, **kwargs):
        sentence, word = args
        syn = SynonymSubstituition.get_syn(sentence, word)
        syn = ','.join(syn.split(',')[0:SynonymSubstituition.num_syns])
        # syn = syn[0:SynonymSubstituition.num_syns]
        # sentence = sentence.replace(word, "{}: {}".format(word, str(syn)))
        replace_str = "{} ({})".format(ColorOutput(word, 'bold'), ColorOutput(syn, 'emphasis'))
        sentence = sentence.replace(word, replace_str)
        return sentence

    @staticmethod
    def get_syn(sentence, word):
        return WordNet.get_syn(word, types=[SynonymSubstituition.get_type(sentence, word)])[0]

    @staticmethod
    def get_type(sentence, word):
        return PennTreebank.get_pos_tag(
            SynonymSubstituition.get_word_pos(PennTreebank.get_pos(sentence), word))

    @staticmethod
    def get_word_pos(sentence_pos, word):
        for wd, pos in sentence_pos:
            if wd == word:
                return pos

    @staticmethod
    def similar(word_1, word_2):
        return SequenceMatcher(None, word_1, word_2).ratio()
