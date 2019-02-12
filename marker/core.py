# App logic
from __future__ import print_function
import os
from . import keys
from . import readchar
from . import line
from . import renderer
from .filter import filter_lines

from sys import version_info, platform

if version_info[0] == 2:
    keyboard_input = raw_input
else:
    keyboard_input = input


def read_line(state):
    ''' parse user input '''
    output = None
    while True:
        c = readchar.get_symbol()
        #print(c)
        if c == keys.ENTER:
            if state.get_matches():
                output = state.get_selected_match()
            break
        elif c == keys.CTRL_C or c == keys.ESC:
            state.reset_input()
            break
        elif c == keys.CTRL_U:
            state.clear_input()
        elif c == keys.BACKSPACE:
            state.set_input(state.input[0:-1])
        elif c == keys.UP:
            state.select_previous()
        elif c == keys.DOWN or c == keys.TAB:
            state.select_next()
        elif c <= 126 and c >= 32:
            state.set_input(state.input + chr(c))
        renderer.refresh(state)
    return output

class State(object):
    '''
    The app State, including user written characters, matched lines, and
    selected one
    '''

    def __init__(self, bookmarks, default_input):
        self.bookmarks = bookmarks
        self._selected_line_index = 0
        self.matches = []
        self.default_input = default_input
        self.set_input(default_input)

    def get_matches(self):
        return self.matches

    def reset_input(self):
        self.input = self.default_input

    def set_input(self, input):
        self.input = input if input else ""
        self._update()

    def clear_input(self):
        self.set_input("")

    def clear_selection(self):
        self._selected_line_index = 0

    def select_next(self):
        self._selected_line_index = (self._selected_line_index + 1) % len(self.matches) if len(self.matches) else 0

    def select_previous(self):
        self._selected_line_index = (self._selected_line_index - 1) % len(self.matches) if len(self.matches) else 0

    def _update(self):
        self.matches = filter_lines(self.bookmarks, self.input)
        self._selected_line_index = 0

    def get_selected_match(self):
        if len(self.matches):
            return self.matches[self._selected_line_index]
        else:
            raise 'No matches found'
