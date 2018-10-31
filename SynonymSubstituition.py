

import re
import pandas as pd
from difflib import SequenceMatcher
from nltk import word_tokenize
from pdb import set_trace as st

from WordNet import WordNet
from PennTreebank import PennTreebank
from ColorOutput import ColorOutput
from CheckRareWord import CheckRareWord


class SynonymSubstituition:

    difficulty_level = 10e3  # 2e3
    num_syns_display = 4

    similarity = .8

    def __new__(cls, sentence, word=None, difficulty_level=difficulty_level):
        sentence = SynonymSubstituition.clean(sentence)
        word = None if not word else SynonymSubstituition.clean(word)
        SynonymSubstituition.difficulty_level = difficulty_level
        if not word:
            for word in sentence.strip().split(' '):
                sentence = SynonymSubstituition.replace_in_word(sentence, word)
        else:
            sentence = SynonymSubstituition.replace_in_word(sentence, word, use_common=True)
        return sentence

    @staticmethod
    def replace_in_word(sentence, word, use_common=False):
        orig_word = word
        word = SynonymSubstituition.clean(word)
        sentence2 = ''
        if use_common or CheckRareWord(word) > SynonymSubstituition.difficulty_level:
            syn = SynonymSubstituition.get_syn(SynonymSubstituition.clean(sentence), word)
            syn = ','.join(syn.split(',')[0:SynonymSubstituition.num_syns_display])
            replace_str = "{} [{}]".format(ColorOutput(orig_word, 'bold'), ColorOutput(syn, 'emphasis'))
            for wd in sentence.split(' '):
                if SynonymSubstituition.clean(wd) == word:
                    sentence2 += replace_str
                else:
                    sentence2 += wd
                sentence2 += ' '
        return sentence2 if sentence2 != '' else sentence

    @staticmethod
    def get_syn(sentence, word):
        # return WordNet.get_syn(word, types=[SynonymSubstituition.get_type(sentence, word)])[0]
        # st()
        word = word.split(' ')[0]
        syn = WordNet.get_syn(word, types=[SynonymSubstituition.get_type(sentence, word)])
        if len(syn) == 0:
            syn = WordNet.get_syn(word)  # get all syns, ranked by general commonality (not wd specific)
        if len(syn) > 0:
            syn = pd.Series(syn)
            try:
                syn = syn[syn != word].unique()
            except:
                st()
            syn2 = []
            for i in range(len(syn)):
                if len(syn[i].split(', ')) > 0:
                    syn[i] = syn[i].split(', ')
                    key = lambda x: CheckRareWord(SynonymSubstituition.clean(x).split(' ')[0])
                    for wd in sorted(syn[i], key=key):
                        syn2.append(wd.strip())
                else:
                    syn2.append(syn[i].strip())
        return ', '.join(syn2[0:SynonymSubstituition.num_syns_display]) if len(syn) > 0  \
               else '?'

    @staticmethod
    def get_type(sentence, word):
        return PennTreebank.get_pos_tag(
            SynonymSubstituition.get_word_pos(PennTreebank.get_pos(sentence), word))

    @staticmethod
    def get_word_pos(sentence_pos, word):
        word = word.split(' ')[0]
        for wd, pos in sentence_pos:
            if SynonymSubstituition.clean(wd) == word:
                return pos
        print('ERROR: word "{}" not found in pos-tagged sentence'.format(word))
        return 'NN'

    @staticmethod
    def similar(word_1, word_2):
        return SequenceMatcher(None, word_1, word_2).ratio()

    @staticmethod
    def clean(string):
        return ' '.join(re.findall('[a-z]+', string.strip().lower()))
