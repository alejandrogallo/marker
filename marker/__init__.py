from .core import (State, read_line)
from . import line


def pick(search, options):
    lines = [line.Line(opt, i) for i, opt in enumerate(options)]
    state = State(lines, search)
    # draw the screen (prompt + matchd marks)
    renderer.refresh(state)
    # wait for user input(returns selected mark)
    rline = read_line(state)
    # clear the screen
    renderer.erase()
    if not rline:
        return state.input
    return (rline.index, rline.header)
