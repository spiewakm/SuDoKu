#!/opt/anaconda3/bin/python

"""
glowna aplikacja do uruchomienia Sudoku
"""

import sys
from PyQt4 import QtGui
from sudoku.SudokuMainWindow import SudokuMainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    form = SudokuMainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()    