"""
Class with game's information 
"""

about = """\
SuDoKu is a simple Sudoku game, developed by Martyna Śpiewak in Python.
"""


keys = [
    ('Up arrow', 'Move cursor up'),
    ('Down arrow', 'Move cursor down '),
    ('Right arrow', 'Move cursor right'),
    ('Left arrow', 'Move cursor left'),
    ('Backspace/Delete', 'Delete a digit from the cell'),
    ('Ctrl+C', 'Check the solution'), 
    ('Ctrl+M', "Show the one cell's solution"),
    ('Ctrl+S', "Show the game's solution"),
    ('Ctrl+R', 'Restart game'),
    ('Ctrl+N', 'New game'),
    ('Ctrl+O', 'Options game'),
    ('Ctrl+Q', 'Quit'),
    ('F1', 'About SuDoKu'),
    ]
    
rules = """\
Each puzzle consists of a 9x9 grid containing given clues in various places. 

The object is to fill all empty squares so that the numbers 1 to 9 appear exactly once in each row, column and 3x3 box.
"""
    
from PyQt4 import QtGui
from PyQt4 import QtCore
import qdarkstyle

class AboutGame(QtGui.QDialog):
    
    def __init__(self):
        super(AboutGame, self).__init__()
        self.setWindowTitle('About SuDoKu')
        self.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
        
        aboutPage = QtGui.QWidget(self)
        logo = QtGui.QLabel()
        pixmap = QtGui.QPixmap('sudoku/sudoku.png')
        logo.setPixmap(pixmap)
        
        aboutLabel = QtGui.QLabel(about)
        
        aboutLayout = QtGui.QVBoxLayout()
        aboutLayout.addSpacing(30)
        aboutLayout.addWidget(logo, 0, QtCore.Qt.AlignCenter)
        aboutLayout.addWidget(aboutLabel, 0, QtCore.Qt.AlignCenter)
        aboutPage.setLayout(aboutLayout)
        
        sudoku = QtGui.QLabel()
        pixmap2 = QtGui.QPixmap('sudoku/sudoku2.png')
        sudoku.setPixmap(pixmap2)
        
        rulePage = QtGui.QWidget(self)
        ruleLabel = QtGui.QLabel(rules)
        ruleLayout = QtGui.QVBoxLayout()
        ruleLayout.addWidget(sudoku, 0, QtCore.Qt.AlignCenter)
        ruleLayout.addSpacing(30)
        ruleLayout.addWidget(ruleLabel)
        
        
        keysPage = QtGui.QWidget(self)
        keysLayout = QtGui.QGridLayout()
        i = 0
        for key, desc in keys:
            keysLayout.addWidget(QtGui.QLabel(key), i, 0)
            keysLayout.addWidget(QtGui.QLabel(desc), i, 1)
            i += 1
        keysPage.setLayout(keysLayout)
    
        
        rulePage.setLayout(ruleLayout)
        
        tabs = QtGui.QTabWidget(self)        
        tabs.addTab(aboutPage, 'About')
        tabs.addTab(rulePage, 'Game Rules')
        tabs.addTab(keysPage, 'Keys')
        
        okbutton = QtGui.QPushButton('OK')
        self.connect(okbutton, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('accept()'))
        
        bbox = QtGui.QHBoxLayout()
        bbox.addStretch()
        bbox.addWidget(okbutton)
        bbox.addStretch()
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(tabs)
        layout.addLayout(bbox)
        self.setLayout(layout)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = AboutGame()
    dialog.exec_()      