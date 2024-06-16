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
    'large': [5, 7],
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
    KEY_0: 'z',
}

GAME_P1_TURNS = 16
GAME_P1_TIME_LIMIT = 40000
GAME_WORD_SIZE = 6
GAME_HEROES = [
    { 'name': 'HHC', 'nick': 'Honghong Chou' },
    { 'name': 'HJJ', 'nick': 'Huang Jijing' },
    { 'name': 'QMY', 'nick': 'Qiu Miao' },
    { 'name': 'TZY', 'nick': 'Tangent Y' },
    { 'name': 'WLH', 'nick': 'Lu Kehan' },
    { 'name': 'XJY', 'nick': 'Sexual Education' },
    { 'name': 'ZKY', 'nick': 'Joker Rain' },
]
GAME_HEROES_NUM = len(GAME_HEROES)
GAME_P1_SN_SCORE_L = 2
GAME_P1_SN_SCORE_R = 10
GAME_P1_ME_SCORE_L = 5
GAME_P1_ME_SCORE_R = 7
GAME_P1_ME_SCORE_XTRA_CHEAT_L = 6
GAME_P1_ME_SCORE_XTRA_CHEAT_R = 30
GAME_P1_ME_SCORE_XTRA_YUE = 6
GAME_TEXTS = {
    'SN_SCORED': ['Yes yes!', 'Em. Dui. Yes.'],
    'ME_SCORED': [
        ['Ha hie!!!'],
        ['He he he~~'],
        ['OOh yes yes yes!'],
        ['Siu!!!'],
        ['Ha ha ha!'],
        ['Oh~~~'],
        ['How am I?'],
    ],
}
GAME_EAT_MAX = [12, 8, 5, 7, 5, 6, 7]
GAME_BAD_WORDS = ['god', 'leo', 'siu', 'kobe', 'shit', 'damn', 'mamba', 'nigga', 'fuck', 'jesus', 'joker', 'damnit', 'nigger']
GAME_SEXY_WORDS = ['sex', 'sexy', 'dick', 'fuck', 'pussy', 'sperm', 'virgin', 'vagina']
GAME_P1_ME_SCORE_XTRA_BAD_WORDS_M = len(GAME_BAD_WORDS) * 2
GAME_P1_ME_SCORE_XTRA_SEXY_WORDS_M = len(GAME_SEXY_WORDS) * 3
GAME_CHEAT_POSS = .6
GAME_ZERO_POSS = .7 / 2
GAME_P1_DISPLAY_SCORES  = 0b1
GAME_P1_DISPLAY_STATUS  = 0b10
GAME_P1_DISPLAY_WS      = 0b100
GAME_P1_DISPLAY_WI      = 0b1000
GAME_P1_DISPLAY_EATEN   = 0b10000
GAME_P1_DISPLAY_ALL     = 0b11111
