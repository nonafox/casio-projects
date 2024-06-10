from gint import *
from conf import *
from funcs import *
from imgs import *
from data_helper import *
import time
import random

curr_hero, curr_hero_name = '', ''
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
        dsubimage(0, 20, GAME_HEROES[curr_hero]['img'], 0, 10, SCREEN_WIDTH, SCREEN_HEIGHT - 10)
        dupdate()
        key = wait_any_key()
        if key == KEY_EXE:
            return
        elif key == KEY_RIGHT:
            data_set('hero', carousel(curr_hero, 1, 0, GAME_HEROES_NUM - 1))
        elif key == KEY_LEFT:
            data_set('hero', carousel(curr_hero, - 1, 0, GAME_HEROES_NUM - 1))

def game_p1_scores():
    global a, b, curr_hero_name
    my_text(.5, 5, f'SN {a} - {b} {curr_hero_name}', RGB_WHITE, FONT_LARGE)
def game_p1_turn_dead(score: int = random.randint(GAME_P1_SN_SCORE_L, GAME_P1_SN_SCORE_R)):
    global a, b, w, wa, ws, wi
    a += score
    game_p1_scores()
    my_text(0, 20, random.choice(GAME_TEXTS['SN_SCORED']), RGB_BLACK, FONT_SMALL)
    my_text(.5, .8, '/'.join(wa), RGB_BLACK, FONT_LARGE)
    dupdate()
    wait_key(KEY_EXE)
def game_p1_turn_win(score: int = random.randint(GAME_P1_ME_SCORE_L, GAME_P1_ME_SCORE_R)):
    global a, b, w, wa, ws, wi, curr_hero
    b += score
    game_p1_scores()
    my_text(0, 20, random.choice(GAME_TEXTS['ME_SCORED'][curr_hero]), RGB_BLACK, FONT_SMALL)
    my_text(.5, .8, '/'.join(wa), RGB_BLACK, FONT_LARGE)
    dupdate()
    wait_key(KEY_EXE)
def game_p1_notice(text: str):
    my_text(0, 20, text, RGB_BLACK, FONT_SMALL)
    dupdate()
    wait_key(KEY_EXE)
def game_p1_turn(i: int):
    global a, b, w, wa, ws, wi, curr_hero_name, eaten
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
        game_p1_scores()
        my_text(0, 20, f'{i + 1}/{GAME_P1_TURNS} {tl}s', RGB_BLACK, FONT_SMALL)
        my_text(.5, .6, ws, RGB_BLACK, FONT_LARGE)
        my_text(.5, .8, wi, RGB_BLACK, FONT_LARGE)
        my_text(.5, .9, eaten, RGB_BLACK, FONT_LARGE)
        dupdate()
        if tl <= 0:
            game_p1_turn_dead()
            return
        key = wait_any_key()
        if key == KEY_EXE:
            if wi == 'yue':
                wi = ''
                eaten = ''
                game_p1_notice('Yue!!!')
                game_p1_turn_win(GAME_P1_ME_SCORE_XTRA_YUE)
            elif wi in GAME_BAD_WORDS:
                wi = ''
                game_p1_notice('Dont say that word!!!')
                game_p1_turn_win(random.randint(GAME_P1_ME_SCORE_XTRA_BAD_WORDS_L, GAME_P1_ME_SCORE_XTRA_BAD_WORDS_R))
            elif wi == 'cheat':
                wi = ''
                if curr_hero == 3 or poss(GAME_CHEAT_POSS):
                    game_p1_notice('Genius!')
                    game_p1_turn_win(random.randint(GAME_P1_ME_SCORE_XTRA_CHEAT_L, GAME_P1_ME_SCORE_XTRA_CHEAT_R))
                else:
                    game_p1_notice('NO cheating!')
            else:
                if len(eaten + wi) <= GAME_EAT_MAX[curr_hero]:
                    eaten += wi
                else:
                    eaten = ''
                    game_p1_notice('Full and yued...')
                game_p1_turn_dead()
            return
        elif key == KEY_DEL:
            if len(wi):
                if wi[- 1] in w:
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
    for i in range(GAME_P1_TURNS):
        game_p1_turn(i)

def go():
    index_select_roles()
    game()
