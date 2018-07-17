

from SynonymSubstituition import SynonymSubstituition
from CheckRareWord import CheckRareWord


if __name__ == '__main__':
    sentence = 'And now for something completely different'  # 'the convict went to jail'
    word = 'completely'  # 'convict'
    print(SynonymSubstituition(sentence, word))

    print(CheckRareWord('dog'))


