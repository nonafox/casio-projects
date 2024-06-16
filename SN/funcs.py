from casioplot import *
from gint import *
from conf import *

my_texts = {}

def carousel(val: int, step: int, limit_l: int = 0, limit_r: int = 0):
    val += step
    if val > limit_r:
        val = limit_l
    elif val < limit_l:
        val = limit_r
    return val
def color_invert(color: RGB_BLACK | RGB_WHITE):
    if color == RGB_BLACK:
        return RGB_WHITE
    return RGB_BLACK
def poss(poss: float):
    return poss * 100 >= random.randint(0, 100)

def wait_key(key: int):
    cleareventflips()
    clearevents()
    while 1:
        ev = pollevent()
        if ev.type == KEYEV_DOWN and ev.key == key:
            break
def wait_any_key():
    cleareventflips()
    clearevents()
    while 1:
        ev = pollevent()
        if ev.type == KEYEV_DOWN:
            return ev.key
def translate_key(key: int):
    if key in KEYS_TABLE:
        return KEYS_TABLE[key]
    else:
        return ''

def calc_text_pos(axis: int, offset: int, text: str, size: str) -> int:
    n = len(text)
    if axis == 0:
        return int((SCREEN_SIZES[0] - n * FONT_SIZES[size][0] - FONT_MARGIN_WIDTH * (n - 1)) * offset)
    else:
        return int((SCREEN_SIZES[1] - FONT_SIZES[size][1]) * offset)

def my_text(x: int, y: int, text: str, color: RGB_BLACK | RGB_WHITE, size: str):
    x1, y1 = x, y
    if 0 < x < 1:
        x1 = calc_text_pos(0, x, text, size)
    if 0 < y < 1:
        y1 = calc_text_pos(1, y, text, size)
    myprofile = [x1, y1, text, color, size]
    if (x, y) in my_texts:
        profile = my_texts[x, y]
        if profile != myprofile:
            draw_string(profile[0], profile[1], profile[2], color_invert(profile[3]), profile[4])
        del my_texts[x, y]
    draw_string(x1, y1, text, color, size)
    my_texts[x, y] = myprofile
