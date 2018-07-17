

import os
import pickle
from pdb import set_trace as st

class CheckRareWord:
    """ larger number is LESS frequent word """

    max_freq = 99e10
    word_freq_path = '100k_most_common.txt'
    word_freq = None


    def __new__(cls, word):
        if not CheckRareWord.word_freq:
            CheckRareWord.word_freq =  \
                CheckRareWord.get_word_freq(CheckRareWord.word_freq_path)
        if word in CheckRareWord.word_freq:
            return CheckRareWord.word_freq[word]
        else:
            return CheckRareWord.max_freq

    @staticmethod
    def get_word_freq(word_freq_path):
        word_freq_path_pik = word_freq_path.replace('.txt', '.pik')
        if os.path.exists(word_freq_path_pik):
            with open(word_freq_path_pik, 'rb') as rf:
                word_freq = pickle.load(rf)
        else:
            with open(word_freq_path, 'r', encoding='utf-8') as rf:
                word = [x.strip() for x in rf.readlines()]
                word_freq = dict([[word[i], i] for i in range(0, len(word))])
            with open(word_freq_path_pik, 'wb') as wf:
                pickle.dump(word_freq, wf)
        return word_freq
