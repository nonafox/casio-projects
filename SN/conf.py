from gint import *
from imgs import *
import random

RGB_WHITE = (255, 255, 255)
RGB_BLACK = (0, 0, 0)

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
SCREEN_SIZES = [SCREEN_WIDTH, SCREEN_HEIGHT]

FONT_MARGIN_WIDTH = 1
FONT_SIZES = {
    'small': [3, 5],
    'medium': [4, 6],
    'large': [5, 7]
}
FONT_SMALL = 'small'
FONT_MEDIUM = 'medium'
FONT_LARGE = 'large'

FILE_WORDS = 'SN/data/words/words.txt'
FILE_WORDS_LINES = 763
FILE_WORDS_ISOMERS = 'SN/data/words/isomers.json'
FILE_GAME = 'SN/data/game.json'

KEYS_TABLE = {
    KEY_XOT: 'a',
    KEY_LOG: 'b',
    KEY_LN: 'c',
    KEY_SIN: 'd',
    KEY_COS: 'e',
    KEY_TAN: 'f',
    KEY_FRAC: 'g',
    KEY_SWITCH: 'h',
    KEY_LEFTP: 'i',
    KEY_RIGHTP: 'j',
    KEY_COMMA: 'k',
    KEY_ARROW: 'l',
    KEY_7: 'm',
    KEY_8: 'n',
    KEY_9: 'o',
    KEY_4: 'p',
    KEY_5: 'q',
    KEY_6: 'r',
    KEY_TIMES: 's',
    KEY_DIV: 't',
    KEY_1: 'u',
    KEY_2: 'v',
    KEY_3: 'w',
    KEY_PLUS: 'x',
    KEY_MINUS: 'y',
    KEY_0: 'z'
}

GAME_P1_TURNS = 5
GAME_P1_TIME_LIMIT = 30000
GAME_WORD_SIZE = 6
GAME_HEROES = [
    { 'name': 'HHC', 'img': IMG_ROLE_11 },
    { 'name': 'HJJ', 'img': IMG_ROLE_13 },
    { 'name': 'QMY', 'img': IMG_ROLE_36 },
    { 'name': 'TZY', 'img': IMG_ROLE_39 },
    { 'name': 'WLH', 'img': IMG_ROLE_40 },
    { 'name': 'XJY', 'img': IMG_ROLE_42 },
]
GAME_HEROES_NUM = len(GAME_HEROES)
GAME_P1_SN_SCORE_L = 3
GAME_P1_SN_SCORE_R = 5
GAME_P1_ME_SCORE_L = 2
GAME_P1_ME_SCORE_R = 7
GAME_TEXTS = {
    'SN_SCORED': ['Yes yes!', 'Em. Dui. Yes.'],
    'ME_SCORED': [
        ['Ha hie!!!'],
        ['He he he~~'],
        ['OOh yes yes yes!'],
        ['Siu!!!'],
        ['Ha ha ha!'],
        ['Oh~~~'],
    ]
}
