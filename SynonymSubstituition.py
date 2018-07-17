

import pandas as pd
from difflib import SequenceMatcher
from nltk import word_tokenize
from pdb import set_trace as st

from WordNet import WordNet
from PennTreebank import PennTreebank
from ColorOutput import ColorOutput
from CheckRareWord import CheckRareWord


class SynonymSubstituition:

    difficulty_level = 2e3
    num_syns_display = 4

    similarity = .8

    def __new__(cls, sentence, word=None, difficulty_level=difficulty_level):
        SynonymSubstituition.difficulty_level = difficulty_level
        if not word:
            for word in sentence.strip().split(' '):
                sentence = SynonymSubstituition.replace_in_word(sentence, word)
        else:
            sentence = SynonymSubstituition.replace_in_word(sentence, word, use_common=True)
        return sentence

    @staticmethod
    def replace_in_word(sentence, word, use_common=False):
        if use_common or CheckRareWord(word) > SynonymSubstituition.difficulty_level:
            syn = SynonymSubstituition.get_syn(sentence, word)
            syn = ','.join(syn.split(',')[0:SynonymSubstituition.num_syns_display])
            # syn = syn[0:SynonymSubstituition.num_syns]
            # sentence = sentence.replace(word, "{}: {}".format(word, str(syn)))
            replace_str = "{} [{}]".format(ColorOutput(word, 'bold'), ColorOutput(syn, 'emphasis'))
            sentence = sentence.replace(word, replace_str)
        return sentence

    @staticmethod
    def get_syn(sentence, word):
        # return WordNet.get_syn(word, types=[SynonymSubstituition.get_type(sentence, word)])[0]
        syn = WordNet.get_syn(word, types=[SynonymSubstituition.get_type(sentence, word)])
        syn = pd.Series(syn)
        syn = syn[syn != word].unique()
        syn2 = []
        for i in range(len(syn)):
            if len(syn[i].split(', ')) > 0:
                for wd in sorted(syn[i].split(', '),
                                 key=lambda x: CheckRareWord(x)):
                    syn2.append(wd.strip())
            else:
                syn2.append(syn[i].strip())
        st()
        return ', '.join(syn2[0:SynonymSubstituition.num_syns_display]) if len(syn) > 0  \
               else '?'

    @staticmethod
    def get_type(sentence, word):
        return PennTreebank.get_pos_tag(
            SynonymSubstituition.get_word_pos(PennTreebank.get_pos(sentence), word))

    @staticmethod
    def get_word_pos(sentence_pos, word):
        for wd, pos in sentence_pos:
            if wd == word:
                return pos
        st()
        raise Exception('word not found in pos-tagged sentence')

    @staticmethod
    def similar(word_1, word_2):
        return SequenceMatcher(None, word_1, word_2).ratio()
