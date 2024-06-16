from gint import *
from conf import *
from funcs import *
from imgs import *
from data_helper import *
import time
import random
import math

curr_hero, curr_hero_name = '', ''
i, tl = 0, 0
a, b = 0, 0
w, wa, ws, wi = '', '', '', ''
eaten = ''

def index_select_roles():
    global curr_hero, curr_hero_name
    dclear(C_WHITE)
    dimage(0, 0, IMG_ROLE_BG)
    my_text(.5, 5, 'Choose your hero', RGB_WHITE, FONT_LARGE)
    while 1:
        curr_hero = data_get('hero')
        curr_hero_name = GAME_HEROES[curr_hero]['name']
        my_text(.5, .5, GAME_HEROES[curr_hero]['nick'], RGB_BLACK, FONT_LARGE)
        dupdate()
        key = wait_any_key()
        if key == KEY_EXE:
            return
        elif key == KEY_RIGHT:
            data_set('hero', carousel(curr_hero, 1, 0, GAME_HEROES_NUM - 1))
        elif key == KEY_LEFT:
            data_set('hero', carousel(curr_hero, - 1, 0, GAME_HEROES_NUM - 1))

def game_p1_display(flag: int, param = None):
    global a, b, curr_hero_name
    if flag == GAME_P1_DISPLAY_SCORES:
        my_text(.5, 5, f'SN {a} - {b} {curr_hero_name}', RGB_WHITE, FONT_LARGE)
    elif flag == GAME_P1_DISPLAY_STATUS:
        my_text(0, 20, param, RGB_BLACK, FONT_SMALL)
    elif flag == GAME_P1_DISPLAY_WS:
        my_text(.5, .5, param, RGB_BLACK, FONT_LARGE)
    elif flag == GAME_P1_DISPLAY_WI:
        my_text(.5, .7, param, RGB_BLACK, FONT_LARGE)
    elif flag == GAME_P1_DISPLAY_EATEN:
        my_text(.5, .95, param, RGB_WHITE, FONT_LARGE)
def game_p1_display_default(flags: int = GAME_P1_DISPLAY_ALL):
    global i, tl
    if flags & GAME_P1_DISPLAY_SCORES:
        game_p1_display(GAME_P1_DISPLAY_SCORES)
    if flags & GAME_P1_DISPLAY_STATUS:
        game_p1_display(GAME_P1_DISPLAY_STATUS, f'{i + 1}/{GAME_P1_TURNS} {tl}s')
    if flags & GAME_P1_DISPLAY_WS:
        game_p1_display(GAME_P1_DISPLAY_WS, ws)
    if flags & GAME_P1_DISPLAY_WI:
        game_p1_display(GAME_P1_DISPLAY_WI, wi)
    if flags & GAME_P1_DISPLAY_EATEN:
        game_p1_display(GAME_P1_DISPLAY_EATEN, eaten)
def game_p1_turn_dead(score: int = random.randint(GAME_P1_SN_SCORE_L, GAME_P1_SN_SCORE_R)):
    global a, b, w, wa, ws, wi, eaten
    a += score
    game_p1_display(GAME_P1_DISPLAY_SCORES)
    game_p1_display(GAME_P1_DISPLAY_STATUS, random.choice(GAME_TEXTS['SN_SCORED']))
    game_p1_display(GAME_P1_DISPLAY_WS, ws)
    game_p1_display(GAME_P1_DISPLAY_WI, '/'.join(wa))
    game_p1_display(GAME_P1_DISPLAY_EATEN, eaten)
    dupdate()
    wait_key(KEY_EXE)
def game_p1_turn_win(score: int = random.randint(GAME_P1_ME_SCORE_L, GAME_P1_ME_SCORE_R)):
    global a, b, w, wa, ws, wi, curr_hero, eaten
    b += score
    game_p1_display(GAME_P1_DISPLAY_SCORES)
    game_p1_display(GAME_P1_DISPLAY_STATUS, random.choice(GAME_TEXTS['ME_SCORED'][curr_hero]))
    game_p1_display(GAME_P1_DISPLAY_WS, ws)
    game_p1_display(GAME_P1_DISPLAY_WI, '/'.join(wa))
    game_p1_display(GAME_P1_DISPLAY_EATEN, eaten)
    dupdate()
    wait_key(KEY_EXE)
def game_p1_notice(text: str, display_flags: int = GAME_P1_DISPLAY_ALL):
    game_p1_display_default(display_flags)
    game_p1_display(GAME_P1_DISPLAY_STATUS, text)
    dupdate()
    wait_key(KEY_EXE)
def game_p1_turn():
    global i, a, b, w, wa, ws, wi, curr_hero_name, eaten, tl
    dclear(C_WHITE)
    dimage(0, 0, IMG_ROLE_BG)
    w = word()
    wa = word_ans(w)
    ws = word_scramble(w)
    wi = ''
    t = time.ticks_ms()
    while 1:
        dt = time.ticks_ms() - t
        tl = int((GAME_P1_TIME_LIMIT - dt) / 1000)
        game_p1_display_default()
        dupdate()
        if tl <= 0:
            game_p1_turn_dead()
            return
        key = wait_any_key()
        if key == KEY_EXE:
            if wi == 'yue':
                eaten = ''
                game_p1_notice('Yue!!!', GAME_P1_DISPLAY_EATEN)
                wi = ''
                if curr_hero == 6:
                    game_p1_turn_dead(GAME_P1_ME_SCORE_XTRA_YUE)
                else:
                    game_p1_turn_win(GAME_P1_ME_SCORE_XTRA_YUE)
            elif curr_hero == 5 and wi in GAME_SEXY_WORDS:
                game_p1_notice('Ah~~ ahhh~~~')
                wi = ''
                game_p1_turn_win(random.randint(GAME_SEXY_WORDS.index(wi), GAME_P1_ME_SCORE_XTRA_SEXY_WORDS_M))
            elif wi in GAME_BAD_WORDS:
                game_p1_notice('Dont say that word!!!')
                wi = ''
                game_p1_turn_win(random.randint(GAME_BAD_WORDS.index(wi), GAME_P1_ME_SCORE_XTRA_BAD_WORDS_M))
            elif wi == 'cheat':
                if curr_hero == 3 or poss(GAME_CHEAT_POSS):
                    game_p1_notice('Genius!')
                    game_p1_turn_win(random.randint(GAME_P1_ME_SCORE_XTRA_CHEAT_L, GAME_P1_ME_SCORE_XTRA_CHEAT_R))
                else:
                    game_p1_notice('NO cheating!')
                wi = ''
            elif (curr_hero == 4 and wi == 'bdbd') or wi == 'bdbdbd':
                game_p1_notice('Inverse!')
                wi = ''
                a, b = b, a
            elif wi == 'math':
                game_p1_notice('Math power!')
                wi = ''
                if poss(GAME_ZERO_POSS * 2) if curr_hero == 1 else poss(GAME_ZERO_POSS):
                    a = b = 0
                else:
                    gcd = math.gcd(a, b)
                    a //= gcd
                    b //= gcd
            else:
                if len(eaten + wi) <= GAME_EAT_MAX[curr_hero]:
                    eaten += wi
                else:
                    eaten = ''
                    game_p1_notice('Full and yued...', GAME_P1_DISPLAY_EATEN)
                game_p1_turn_dead()
            return
        elif key == KEY_DEL:
            if len(wi):
                if wi[- 1] in w and ws.count(wi[- 1]) < w.count(wi[- 1]):
                    ws += wi[- 1]
                else:
                    eaten += wi[- 1]
                wi = wi[0 : - 1]
        else:
            ch = translate_key(key)
            if ch in ws:
                wi += ch
                ws = ws.replace(ch, '', 1)
            elif ch in eaten:
                wi += ch
                eaten = eaten.replace(ch, '', 1)
        if len(wi) == GAME_WORD_SIZE and wi in wa:
            b += random.randint(GAME_P1_ME_SCORE_L, GAME_P1_ME_SCORE_R)
            game_p1_turn_win()
            return
def game():
    global i
    for i in range(GAME_P1_TURNS):
        game_p1_turn()

def go():
    index_select_roles()
    game()
