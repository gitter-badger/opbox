import os

# Get parameters from console
height, width = os.popen('stty size', 'r').read().split()
height = int(height)
width = int(width)

class ConsoleInterface(object):
    """A class that makes the CLI."""
    def __init__(self):
        self.width = width
        self.height = height
        self.col_num = 8

    def printRow(self, row):
        #col_width = max(len(word) for word in row) + 2
        col_width = self.width/self.col_num;
        print ''.join(word[0:col_width-2].ljust(col_width) for word in row) #joins columns truncating at 8 chars.

    def rprintRow(self, row):
        #col_width = max(len(word) for word in row) + 2
        col_width = self.width/self.col_num;
        print ''.join(word[0:col_width-2].rjust(col_width) for word in row) #joins columns truncating at 8 chars.

    def cprintRow(self, row):
        #col_width = max(len(word) for word in row) + 2
        col_width = self.width/self.col_num;
        print ''.join(word[0:col_width-2].center(col_width) for word in row) #joins columns truncating at 8 chars.

    def printRowEntireWords(self, row):
        #col_width = max(len(word) for word in row) + 2
        col_width = self.width/self.col_num;
        print ''.join(word.ljust(col_width) for word in row) #joins columns NOT truncating

    def printCenteredWithSymbol(self, text, symbol):
        # prints text in the center of a terminal surrounded by repetitions of symbol (multiple characters accepted)
        if text == '':
            text = ' '
            to_print = symbol * ((self.width - len(text))/(len(symbol)))
        else:
            to_print = symbol * ((self.width - len(text) - 2)/(2*len(symbol))) + ' ' + text + ' ' + symbol * ((self.width - len(text) - 1)/(2*len(symbol)))
        print to_print
        return to_print

    def newLine(self):
        empty_row = ['','','','','','','','']
        self.printRow(empty_row)

    def initInterface(self):
        std_row = ['AAAAAAAA','BBBBBBBB','CCCCCCCC','DDDDDDDD','EEEEEEEE','FFFFFFF','GGGGGGGG','HHHHHHHH']
        data_row = ['','','','','','','','']

        os.system('clear')
        self.printCenteredWithSymbol('', ' ')
        self.printCenteredWithSymbol('Welcome to OpBox v0.0', ' ')
        self.printCenteredWithSymbol('contact@opbox.org', ' ')
        self.newLine() 
        self.printCenteredWithSymbol('', '=')
        self.printRow(['Date: ','12/11/15','','Start time: ','13:34:33','','Routine: ','03A'])
        self.printCenteredWithSymbol('', '=')
        self.newLine()
        self.printCenteredWithSymbol('MEASUREMENTS', '  .  ')
        self.newLine()
        self.cprintRow(['Time','',   'Temp[oC]','','FBar','','LInt[lx]',''])
        self.cprintRow(['13:34:33','','23.3','','20.2','','56',''])
        self.cprintRow(['13:34:33','','23.2','','6.7','','56',''])
        self.cprintRow(['13:34:34','','23.3','','0.0','','59',''])
        self.newLine()
        self.newLine()
#Test code

