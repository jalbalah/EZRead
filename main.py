

from SynonymSubstituition import SynonymSubstituition


if __name__ == '__main__':
    sentence = 'And now for something completely different'  # 'the convict went to jail'
    word = 'completely'  # 'convict'
    # sentence = 'recitation'
    # word = sentence
    print(SynonymSubstituition(sentence, word))