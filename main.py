

from SynonymSubstituition import SynonymSubstituition
from CheckRareWord import CheckRareWord


if __name__ == '__main__':
    print('\nThreshold select word...')
    sentence = 'and now for something completely different'  # 'the convict went to jail'
    print(SynonymSubstituition(sentence))

    print('\nExplicitly select word...')
    word = 'different'
    print(SynonymSubstituition(sentence, word))


