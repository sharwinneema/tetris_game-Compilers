import sys
sys.path.append('../')
from game_engine.engine import *

#PRIMITIVE:
Somename = 0
Someothername = 1
difficulty = 500
fg_color = 1
bg_color = 4
speed_increase_factor = 1
speed_decrease_factor = 1
direction = 1
shadow = 0
next = 0

#FUNCTIONS:
def Func2():
    Someothername = Someothername + Somename

def run():
    Somename = tetris_engine.move_piece(direction = 1)

def Func3():
    while 3 + 3 :
        while 3 + 3 :
            Someothername = 5


#ENGINE:
if __name__ == '__main__':
	tetris_engine = TetrisEngine(height = 20, width = 20, fg_color = fg_color, bg_color = bg_color, move_down_duration = difficulty)


