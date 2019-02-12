from . import ansi

# CTLR + @
CTRL_AT = 0
CTRL_A = 1
CTRL_B = 2
CTRL_C = 3
CTRL_D = 4
CTRL_E = 5
CTRL_F = 6
CTRL_G = 7
CTRL_H = 8
CTRL_I = 9
TAB = 9
CTRL_J = 10
CTRL_K = 11
CTRL_L = 12
CTRL_M = 13
ENTER = 13
CTRL_N = 14
CTRL_O = 15
CTRL_P = 16
CTRL_Q = 17
CTRL_R = 18
CTRL_S = 19
CTRL_T = 20
CTRL_U = 21
CTRL_V = 22
CTRL_W = 23
CTRL_X = 24
CTRL_Y = 25
CTRL_Z = 26
# ctrl + [
CTRL_LBRACKET = 27
ESC = 27
CTRL_BACKSLASH = 28
# ctrl + ]
CTRL_RBRACKET = 29
CTRL_CARET = 30
CTRL_UNDERSCORE = 31


SPACE  = 64
RIGHT = ansi.cursor.forward()
DOWN = ansi.cursor.down()
UP = ansi.cursor.up()
LEFT = ansi.cursor.back()
BACKSPACE = 127
