from . import ansi

class Line(object):
    '''A Line is composed of the shell command string and an optionnal alias'''
    def __init__(self, header, index):
        self.header = header
        self.index = index

    def __repr__(self):
        return self.header
