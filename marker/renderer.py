import os
from . import ansi
import re
import math
import sys
'''Line line user interface'''

def _get_terminal_columns():
    '''
    get the number of terminal columns, used to determine spanned lines of a
    mark(required for cursor placement)
    '''
    rows, columns = os.popen('stty size', 'r').read().split()
    # the -1 is to keep the line prompt displayed
    return int(rows) - 1, int(columns)

def unicode_length(string):
    if sys.version_info[0] == 2:
        return len(string.decode('utf-8'))
    else:
        return len(string)

def erase():
    '''
    The lineline cursor is always at the first line (Marker prompt)
    Therefore, erasing the current and following lines clear all marker output
    '''
    ansi.move_cursor_line_beggining()
    ansi.erase_from_cursor_to_end()

def refresh(state):
    '''
    Redraw the output, this function will be triggered on every user
    interaction(key pressed)
    '''
    erase()
    lines, num_rows = _construct_output(state)
    for line in lines[:-1]:
        print(line)
    # new new line for the last result
    if(lines):
        sys.stdout.write(lines[-1])
    # go up
    ansi.move_cursor_previous_lines(num_rows - 1)
    # palce the cursor at the end of first line
    ansi.move_cursor_horizontal(len(lines[0])+1)
    ansi.flush()

def _construct_output(state, prompt=" ", max_lines=10):
    rows, columns = _get_terminal_columns()
    ansi_escape = re.compile(r'\x1b[^m]*m')
    def number_of_rows(line):
        line = ansi_escape.sub('', line)
        return int(math.ceil(float(unicode_length(line))/columns))
    displayed_lines = []
    # Number of terminal rows spanned by the output, used to determine how many
    # lines we need to go up(to place the cursor after the prompt) after
    # displaying the output
    num_rows = 0
    prompt_line = prompt + state.input
    displayed_lines.append(prompt_line)
    num_rows += number_of_rows(prompt_line)
    matches = state.get_matches()
    if matches:
        # display lines from Max(0,selected_line_index - 10 +1 ) to
        # Max(10,SelectedLineIndex + 1)
        selected_line_index = matches.index(state.get_selected_match())
        num_results = max_lines
        matches_to_display = []
        while (True):
            filtered_matches = matches[max(0, selected_line_index - num_results + 1):max(num_results, selected_line_index + 1)]
            filtered_matches_rows = sum(number_of_rows(' ' + str(el)) for el in filtered_matches)
            if rows - num_rows < filtered_matches_rows:
                num_results -= 1
            else:
                matches_to_display = filtered_matches
                break
        for index, m in enumerate(matches_to_display):
            fm = ' '+str(m)
            num_rows += number_of_rows(fm)
            # Formatting text(make searched word bold)
            for w in state.input.split(' '):
                if w:
                    fm = fm.replace(w, ansi.bold_text(w))
            # highlighting selected line
            if m == state.get_selected_match():
                fm = ansi.select_text(fm)
            displayed_lines.append(fm)
    else:
        not_found_line = 'Nothing found'
        displayed_lines.append(not_found_line)
        num_rows += number_of_rows(not_found_line)
    return displayed_lines, num_rows

