

import sys

from SynonymSubstituition import SynonymSubstituition
from CheckRareWord import CheckRareWord


if __name__ == '__main__':
    print(SynonymSubstituition(' '.join(sys.argv[1::])))

sentence = "The word you've entered isn't in the thesaurus.  \
            Click on a spelling suggestion below or try again using the search bar above.  \
            Don't be a convict!"
sentence = 'the cell was surrounded by a phospholipid bi-layer'
"""