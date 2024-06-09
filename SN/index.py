from casioplot import *
from gint import *
from conf import *
from funcs import *
from imgs import *
from data_helper import *
import game

dclear(C_WHITE)
dimage(0, 0, IMG_JWHGZS)
dupdate()
wait_key(KEY_EXE)
dclear(C_WHITE)
dimage(0, 0, IMG_SN)
dupdate()
wait_key(KEY_EXE)

game.go()
wait_key(KEY_EXE)
