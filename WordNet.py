

from subprocess import check_output, CalledProcessError
from pdb import set_trace as st


class WordNetHelper:

    @staticmethod
    def shell_command(args):
        try:
            res = check_output(args).decode()
        except CalledProcessError as e:
            res = e.output.decode()
        for r in ['\r', '\n\n']:
            res = res.replace(r, '')
        return res.strip()

    @staticmethod
    def get_syn(word, t):
        res = WordNetHelper.shell_command(['wn', word, '-syns{}'.format(t)])
        res = [x[3::].replace('       =>', '') for x in res.split('Sense')]
        del res[0]
        res = '\n'.join(res).split('\n')
        res2 = []
        for i in list(range(0, len(res))):
            if res[i] == '' or 'Derived from' in res[i]:
                pass
            else:
                res2.append(res[i])
        return res2


class WordNet:

    @staticmethod
    def get_syn(word, types=['n', 'v', 'a', 'r'], most_freq=99):
        s = []
        for t in types:
            syns = WordNetHelper.get_syn(word, t)
            if len(syns) != 0:
                s += syns[0:most_freq]
        return s

    @staticmethod
    def get_freq(word, t):
        res = WordNetHelper.shell_command(['wn', word, '-faml{}'.format(t)])
        res = res[res.find('=') + 2:-1]
        return int(res) if res != '' else 0
