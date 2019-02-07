from . import ansi

class Line(object):
    '''A Line is composed of the shell command string and an optionnal alias'''
    def __init__(self, cmd, alias):
        self.cmd = cmd
        self.alias = alias

    def __repr__(self):
        if self.alias and self.alias != self.cmd:
            return self.cmd + " " + ansi.grey_text(self.alias)
        else:
            return self.cmd

    # def equals(self, mark):
        # return self.cmd == mark.cmd and self.alias == mark.alias
