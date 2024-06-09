from conf import *
from funcs import *
from imgs import *
import random

with open(FILE_WORDS_ISOMERS, 'r') as f:
    __words_isomers = eval(f.read())
with open(FILE_GAME, 'r') as f:
    __data = eval(f.read())

def data_get(key: str):
    global __data
    return __data[key]
def data_set(key: str, val: any):
    global __data
    __data[key] = val
    with open(FILE_GAME, 'w') as f:
        f.write(str(__data))

def word():
    rand = random.randint(0, FILE_WORDS_LINES - 1)
    with open(FILE_WORDS, 'r') as f:
        f.seek((GAME_WORD_SIZE + 1) * rand)
        w = f.readline().strip()
        return w
def word_scramble(w: str):
    r = []
    w = list(w)
    n = len(w)
    while n:
        i = random.randint(0, n - 1)
        r.append(w[i])
        del w[i]
        n -= 1
    return ''.join(r)
def word_ans(w: str):
    global __words_isomers
    w = w.lower()
    if w in __words_isomers:
        return [w] + __words_isomers[w]
    else:
        return [w]
