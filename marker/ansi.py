import sys
import marker.ansilib
# Compatibility for ansilib
sys.modules["ansi"] = marker.ansilib
from marker.ansilib.colour import fg, bg
import marker.ansilib.cursor as cursor

BOLD = str(fg.yellow)
CLEAR_FORMATTING = str(fg.default + bg.default)

FOREGROUND_BLACK = str(fg.black)
BACKGROUND_WHITE = str(bg.red)
SELECT_TEXT_STYLE = str(bg.red + fg.black)


def get_formattings(text):
    if CLEAR_FORMATTING in text:
        return get_formattings(
            text[text.index(CLEAR_FORMATTING)+len(CLEAR_FORMATTING):]
        )
    return ''.join([
        s for s in [BOLD, FOREGROUND_BLACK, BACKGROUND_WHITE]
        if s in text
    ])

def select_text(text):
    return  (
        SELECT_TEXT_STYLE +
        text +
        CLEAR_FORMATTING
    )


def bold_text(text):
    return  (
        BOLD +
        text.replace(
            CLEAR_FORMATTING,
            CLEAR_FORMATTING + BOLD
        ) +
        CLEAR_FORMATTING +
        get_formattings(text)
    )


def move_cursor_horizontal(n):
    sys.stdout.write(cursor.goto(n))


def move_cursor_line_beggining():
    move_cursor_horizontal(0)


def move_cursor_previous_lines(number_of_lines):
    sys.stdout.write(number_of_lines * cursor.prev_line())


def erase_from_cursor_to_end():
    sys.stdout.write(cursor.erase())


def erase_line():
    sys.stdout.write(cursor.erase_line())


def flush():
    sys.stdout.flush()
