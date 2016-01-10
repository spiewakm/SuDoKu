from PyQt4 import QtGui
from PyQt4 import QtCore 
from sudoku.AboutGame import AboutGame
import sudoku.CreateSudoku as cs
import numpy as np
import qdarkstyle

class SudokuMainWindow(QtGui.QMainWindow):
    """
    glowna klasa gry: pojawianie sie okna gry
    """    
    def __init__(self):
        super(SudokuMainWindow, self).__init__()
        
        self.sudokufull= None
        self.sudoku0 = None
        self.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
        self.createMainWindow()
        self.createMenuBar()
        self.newGame()
        
        
    level = 0
    colorCheck0 = QtGui.QColor(255, 0, 0, 200)
    colorSolve0 = QtGui.QColor(0, 102, 51, 255)
    colorCheck = QtGui.QColor(255, 0, 0, 200)
    colorSolve = QtGui.QColor(0, 102, 51, 255)
    changeOptions = False
        
    def createMainWindow(self):
        """
        tworzenie glownego okna gry
        """
        
        self.setGeometry(300, 300, 615, 555)
        self.setWindowTitle('SuDoKu')
        self.setWindowIcon(QtGui.QIcon('sudoku/sudoku.png'))
        
        self.show()
        
    def createMenuBar(self):  
        """
        tworzenie glownego panelu
        """
        newGame = QtGui.QAction('New', self)        
        newGame.setShortcut('Ctrl+N')
        newGame.setStatusTip('New game')
        self.connect(newGame, QtCore.SIGNAL('triggered()'), self.newGame)
        
        optionsGame = QtGui.QAction('Options', self)  
        optionsGame.setShortcut('Ctrl+O')
        optionsGame.setStatusTip('Options game')
        self.connect(optionsGame, QtCore.SIGNAL('triggered()'), self.optionsGame)
        
        exitGame = QtGui.QAction('Close', self)        
        exitGame.setShortcut('Ctrl+Q')
        exitGame.setStatusTip('Close')
        exitGame.triggered.connect(QtGui.qApp.quit)
        
        aboutGame = QtGui.QAction('About', self)        
        aboutGame.setShortcut('F1')
        aboutGame.setStatusTip('About Sudoku')
        self.connect(aboutGame, QtCore.SIGNAL('triggered()'), self.aboutGame)
        
        self.statusBar()

        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(newGame)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(optionsGame)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(exitGame)   
        
        self.helpMenu = self.menuBar().addMenu('Help')
        self.helpMenu.addAction(aboutGame)  
        
        self.setWindowIcon(QtGui.QIcon('sudoku/sudoku.png'))

        
        
    def newGame(self):
        """
        start nowego rozdania sudoku
        """
        newGame = Levels()
        newGame.exec_()
        self.sudokufull = cs.createFullSudoku()
        self.sudoku0 = cs.createSudoku(fullSudoku = self.sudokufull, level = self.level)
        self.createMainPanel(sudoku0 = self.sudoku0, sudokufull = self.sudokufull, level = self.level,
                             colorCheck = self.colorCheck, colorSolve = self.colorSolve)
                
    def aboutGame(self):
        """
        okno na temat sudoku
        """
        openAboutGame = AboutGame()
        openAboutGame.exec_()
        
    def optionsGame(self):
        """
        dodatkowe ustawienia gry
        """
        openOptionsGame = OptionsGame()
        openOptionsGame.exec_()
        
        if self.changeOptions:
            self.createMainPanel(sudoku0 = self.sudoku0, sudokufull = self.sudokufull, 
                             level = self.level, colorCheck = self.colorCheck, colorSolve = self.colorSolve)

                
    def createMainPanel(self, sudoku0, sudokufull, level, colorCheck, colorSolve):
        """
        tworzenie glownego panelu gry
        """
        self.sudokuBoard = SudokuBoard(sudoku0 = sudoku0, sudokufull = self.sudokufull, 
                                       level = self.level, colorCheck = self.colorCheck, colorSolve = self.colorSolve)
        self.sudokuBoard.setFocus()
        
        self.sidePanel = QtGui.QFrame(self)
        self.sidePanel.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)
        self.sidePanel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.createSidePanel()
        
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.sudokuBoard)
        mainLayout.addWidget(self.sidePanel)
        mainLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        
        mainBoard = QtGui.QWidget()
        mainBoard.setLayout(mainLayout)
        self.setCentralWidget(mainBoard)
        
    def createSidePanel(self):
        """
        tworzenie bocznego panelu
        """
        logo = QtGui.QLabel()
        pixmap = QtGui.QPixmap('sudoku/sudoku.png')
        logo.setPixmap(pixmap)
        
        self.restartButton = SizedButton('Restart', QtCore.QSize(90, 40))
        self.restartButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.restartButton.setShortcut('Ctrl+R')
        self.connect(self.restartButton, QtCore.SIGNAL('clicked()'), self.restartGame)
        
        self.checkButton = SizedButton('Check', QtCore.QSize(90, 40))
        self.checkButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkButton.setShortcut('Ctrl+C')
        self.connect(self.checkButton, QtCore.SIGNAL('clicked()'), self.checkGame)
        
        self.solvecellButton = SizedButton('Solve Cell', QtCore.QSize(90, 40))
        self.solvecellButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.solvecellButton.setShortcut('Ctrl+M')
        self.connect(self.solvecellButton, QtCore.SIGNAL('clicked()'), self.solveCellGame) 
        
        self.solveButton = SizedButton('Solve', QtCore.QSize(90, 40))
        self.solveButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.solveButton.setShortcut('Ctrl+S')
        self.connect(self.solveButton, QtCore.SIGNAL('clicked()'), self.solveGame) 
               
        buttonLayout1 = QtGui.QHBoxLayout()
        buttonLayout1.addWidget(self.restartButton)
        buttonLayout2 = QtGui.QHBoxLayout()
        buttonLayout2.addWidget(self.checkButton)
        buttonLayout3 = QtGui.QHBoxLayout()
        buttonLayout3.addWidget(self.solvecellButton)
        buttonLayout4 =  QtGui.QHBoxLayout()
        buttonLayout4.addWidget(self.solveButton)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(buttonLayout2)
        vbox.addSpacing(30)
        vbox.addLayout(buttonLayout3)
        vbox.addSpacing(30)
        vbox.addLayout(buttonLayout4)
        vbox.addSpacing(30)
        vbox.addLayout(buttonLayout1)
        vbox.addSpacing(30)
        vbox.addStretch()
        
        vbox1 = QtGui.QVBoxLayout()
        vbox1.addStretch()
        vbox1.addLayout(vbox)
        vbox1.addStretch()
        self.sidePanel.setLayout(vbox1)
        
    def restartGame(self):
        """
        restartowanie planszy sudoku
        """
        self.createMainPanel(sudoku0 = self.sudoku0, sudokufull = self.sudokufull, level = self.level,
                             colorCheck = self.colorCheck, colorSolve = self.colorSolve)
        
    def solveGame(self):
        """
        pełne rozwiązanie sudoku
        """
        self.createMainPanel(sudoku0 = self.sudokufull, sudokufull = self.sudokufull, level = self.level,
                             colorCheck = self.colorCheck, colorSolve = self.colorSolve)

    def solveCellGame(self):
        """
        rozwiazanie wybranej komórki sudoku
        """
        self.sudokuBoard.keyPress(self, solve = True)

        
    def checkGame(self):
        """
        sprawdzenie czy wypelnione pola sa poprawne
        """
        self.sudokuBoard.checkSudoku(self)
        
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class SizedButton(QtGui.QPushButton):
    def __init__(self, text, size):
        super(SizedButton, self).__init__(text)
        self.size = size
        
    def sizeHint(self):
        return self.size
        
class CreateLevels:
    """
    tworzenie okna poziomow trudnosci:
    0: Simple
    1: Easy
    2: Medium
    3: Hard
    """
    def __init__(self):
        super(CreateLevels, self).__init__()

    def createWindowLevels(self, levels):
        """
        okno wyboru poziomu trudnosci
        """
        levels.setObjectName('levels')
        levels.setWindowModality(QtCore.Qt.WindowModal)
        levels.resize(400, 300)
        levels.setWindowTitle("Difficulty")
        
        levels.setAutoFillBackground(False)
        self.verticalLayoutWidget = QtGui.QWidget(levels)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 50, 200, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.lyLevel = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.lyLevel.setMargin(0)
        self.lyLevel.setObjectName('lyLevel')
        
        self.label = QtGui.QLabel(levels)
        self.label.setGeometry(QtCore.QRect(150, 20, 200, 20))
        self.label.setObjectName("label")

        self.label.setText(QtGui.QApplication.translate("levels", "Select difficulty", None, QtGui.QApplication.UnicodeUTF8))
        QtCore.QMetaObject.connectSlotsByName(levels)    

class Levels(QtGui.QDialog):
    """
    wybor poziomu trudnosci
    """
    def __init__(self):
        super(Levels, self).__init__()
        
        self.level = CreateLevels()
        self.level.createWindowLevels(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.chooseLevel()
        self.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))

        
    def chooseLevel(self):
        """
        wybor poziomu trudnosci
        """
        self.levels = []
        self.levels.append(QtGui.QPushButton("Simple"))
        self.levels.append(QtGui.QPushButton("Easy"))
        self.levels.append(QtGui.QPushButton("Medium"))
        self.levels.append(QtGui.QPushButton("Hard"))
        
        for i in range(0, 4):
            QtCore.QObject.connect(self.levels[i], QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('accept()'))
            QtCore.QObject.connect(self.levels[i], QtCore.SIGNAL("clicked()"), self.funChooseLevel)
            self.level.lyLevel.addWidget(self.levels[i])
        
    def funChooseLevel(self):
        """
        przekazanie ktory poziom zostal wybrany
        """
        cmd = self.sender()
        if cmd.text() == "Simple":
            SudokuMainWindow.level = 0
        if cmd.text() == "Easy":
            SudokuMainWindow.level = 1
        if cmd.text() == "Medium":
            SudokuMainWindow.level = 2
        if cmd.text() == "Hard":
            SudokuMainWindow.level = 3
            
class SudokuBoard(QtGui.QWidget):
    """
    klasa do tworzenia planszy sudoku oraz do 
    wypełniania pól
    """
    def __init__(self, sudoku0, sudokufull, level = 0, 
                 colorCheck = QtGui.QColor(255, 0, 0, 200), colorSolve = QtGui.QColor(60, 179, 113, 200)):
        super(SudokuBoard, self).__init__()
        
        self.sudokufull = sudokufull
        self.sudoku0 = sudoku0
        
        self.colorCheck = colorCheck
        self.colorSolve = colorSolve
        
        self.sudoku = QtGui.QTableWidget(self)
        self.nrow = 9
        self.ncol = 9
        self.sudoku.setRowCount(self.nrow)
        self.sudoku.setColumnCount(self.ncol)
        self.sudoku.resize(51*9, 52*9)
        self.sudoku.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.sudoku.verticalHeader().hide()
        self.sudoku.horizontalHeader().hide()
        
        for i in range(self.nrow):
            self.sudoku.setRowHeight(i, 52)
            for j in range(self.ncol):
                self.sudoku.setColumnWidth(j, 51)
                
                item = QtGui.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.sudoku.setItem(i, j, item)
 
 
        layout = QtGui.QGridLayout()
        layout.addWidget(self.sudoku)
        self.setLayout(layout)
        

        self.emptysudoku = SudokuDraw(self.sudoku)
        self.sudoku.setItemDelegate(self.emptysudoku)
        self.emptysudoku.initGrid(self.sudoku0)
 
        self.optionsSudoku(self.sudoku0)
 
        self.emptyCells = []
        for i in range(9):
            for j in range(9):
                if self.sudoku0[i, j] == 0:
                    self.emptyCells.append((i, j))
 
        self.sudoku.keyPressEvent = self.keyPress
        self.sudoku.checkSudoku = self.checkSudoku
        
    def checkSudoku(self, table):
        """
        funkcja sluzaca do sprawdzania, czy wprowadzone cyfry 
        sa poprawne
        """
        checkall = []
        checktable = []
        for i in range(9):
            for j in range(9):
                if (i, j) in self.emptyCells:
                    tmp = self.sudoku.item(i, j).text()
                    if tmp != str(0) and tmp != '':
                        checkall.append((i, j))
                        if tmp != str(self.sudokufull[i, j]):
                            checktable.append((i, j))
                            
        if checktable:
            for (i, j) in checktable:
                color = self.colorCheck
                self.sudoku.item(i, j).setBackground(color)
        self.sudoku.setCurrentCell(0, 0)
        
        if len(checkall) == len(self.emptyCells): end = True
        else: end = False
        if checktable: 
            checkWindow = CheckWindow(checkbool = False, end = end)
            checkWindow.exec_()
        else: 
            checkWindow = CheckWindow(checkbool = True, end = end)
            checkWindow.exec_()
             
    def keyPress(self, event, solve = False):
        """
        funkcja sluzaca do sterowania wprowadzanymi znakami
        """
        i, j = self.sudoku.currentRow(), self.sudoku.currentColumn()
        
        if solve:
            if (i, j) in self.emptyCells:
                self.sudoku.item(i, j).setText(str(self.sudokufull[i, j]))
                color = self.colorSolve
                self.sudoku.item(i, j).setBackground(color)
                
        else:
            if ord('1') <= event.key() <= ord('9'):
                if (i, j) in self.emptyCells:
                    self.sudoku.item(i, j).setForeground(QtGui.QColor(255, 255, 255))
                    #self.sudoku.item(i, j).setBackground(QtGui.QColor(255, 255, 255, 100))
                    self.sudoku.item(i, j).setText(chr(event.key()))
            elif event.key() == QtCore.Qt.Key_Backspace or event.key() == QtCore.Qt.Key_Delete:
                if (i, j) in self.emptyCells:
                    self.sudoku.item(i, j).setText(str(''))
                    self.sudoku.item(i, j).setBackground(QtGui.QColor(80, 80, 80, 25))
            elif event.key() == QtCore.Qt.Key_Up:
                self.sudoku.setCurrentCell((i - 1) % 9, j)
            elif event.key() == QtCore.Qt.Key_Down:
                self.sudoku.setCurrentCell((i + 1) % 9, j)
            elif event.key() == QtCore.Qt.Key_Right:
                self.sudoku.setCurrentCell(i, (j + 1) % 9)
            elif event.key() == QtCore.Qt.Key_Left:
                self.sudoku.setCurrentCell(i, (j - 1) % 9)
            

 
    def optionsSudoku(self, tablex):
        """
        funckja sluzaca do wypelniania planszy wyjsciowym ukladem 
        cyfr w sudoku
        """
        font = QtGui.QFont()
        font.setFamily("Calibre")
        font.setPointSize(14)
        for i in range(len(tablex[0])):
            for j in range(len(tablex)):
                if tablex[i, j] == 0:
                    self.sudoku.item(i, j).setFont(font)
                    color = QtGui.QColor(225, 255, 255, 255) 
                    self.sudoku.item(i, j).setForeground(color)
                    self.sudoku.item(i, j).setFlags(
                        QtCore.Qt.ItemIsEnabled
                        | QtCore.Qt.ItemIsSelectable
                        | QtCore.Qt.ItemIsEditable
                        | QtCore.Qt.ItemIsDropEnabled
                        | QtCore.Qt.ItemIsDragEnabled)
                else:
                    self.sudoku.item(i, j).setFont(font)
                    color = QtGui.QColor(255, 255, 255, 255) 
                    self.sudoku.item(i, j).setForeground(color)
                    
                    self.sudoku.item(i, j).setText(str(tablex[i, j]))
                    self.sudoku.item(i, j).setFlags(
                        QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
 
class CheckWindow(QtGui.QDialog):
    """
    klasa odpowiedzialna, za pojawiania się okna
    po nacisnieciu przycisku 'Check'
    """
    def __init__(self, checkbool = True, end = False):
        super(CheckWindow, self).__init__()
        self.setWindowTitle('Checking')
        self.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
        
        check = QtGui.QWidget(self)
        
        if checkbool:
            if end:
                x = ['You rock!', 'Good job!', 'You are the master of sudoku!!!']
                xtmp = np.random.choice(x)
                checkLabel = QtGui.QLabel(xtmp)
            else:
                x = ['Good!', 'Well!', "Everything's OK! Continue..."]
                xtmp = np.random.choice(x)
                checkLabel = QtGui.QLabel(xtmp)
        else:
            if end:
                checkLabel = QtGui.QLabel('Oh no! Something went wrong...')
            else:
                checkLabel = QtGui.QLabel('Try again...')
        
        checkLayout = QtGui.QVBoxLayout()
        checkLayout.addWidget(checkLabel, 0, QtCore.Qt.AlignCenter)
        check.setLayout(checkLayout)
        
        okbutton = QtGui.QPushButton('&OK')
        self.connect(okbutton, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('accept()'))
        
        bbox = QtGui.QHBoxLayout()
        bbox.addStretch()
        bbox.addWidget(okbutton)
        bbox.addStretch()
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(check)
        layout.addLayout(bbox)
        self.setLayout(layout)
        
 
 
class SudokuDraw(QtGui.QItemDelegate):
    """
    klasa do rysowania obramowania pola sudoku
    """
    def __init__(self, sudokuBoard):
        super(SudokuDraw, self).__init__()
 
    def initGrid(self, grid):
        self.sudoku0 = grid
 
    def paint(self, object, option, index, color = QtGui.QColor(64, 64, 64, 255)):
        """
        funkcja pomocnicza: do rysowania obramowania planszy
        """
        i, j = index.row(), index.column()
        
        r = option.rect
        x, y, w, h = r.x(), r.y(), r.width() - 2, r.height() - 2
        if self.sudoku0[i, j] != 0:
            object.fillRect(x, y, w, h, color)
        else:
            object.fillRect(x, y, w, h, QtGui.QColor(80, 80, 80, 255))
 
        if i in (0, 3, 6):
            self.borders(object, option, 'up')
            if j in (0, 3, 6):
                self.borders(object, option, 'left') 
            elif j == 8:
                self.borders(object, option, 'right') 
        elif i == 8:
            self.borders(object, option, 'bottom')
            if j in (0, 3, 6):
                self.borders(object, option, 'left')
            elif j == 8:
                self.borders(object, option, 'right')    
        elif j in (0, 3, 6):
            self.borders(object, option, 'left')
        elif j == 8:
            self.borders(object, option, 'right')

            
 
        QtGui.QItemDelegate.paint(self, object, option, index)
        
    def borders(self, object, option, pos):
        """
        funkcja pomocnicza: do rysowania linii
        """
        r = option.rect
        x, y, w, h = r.x(), r.y(), r.width(), r.height()
     
        if pos == 'up':
            x1, y1, x2, y2 = x, y, x + w, y
        elif pos == 'bottom':
            x1, y1, x2, y2 = x, y + h - 0.5, x + w, y + h - 0.5
        elif pos == 'right':
            x1, y1, x2, y2 = x + w - 0.5, y - h, x + w - 0.5, y + h
        elif pos == 'left':
            x1, y1, x2, y2 = x, y , x, y + h
        else:
            return None
     
        pencil = QtGui.QPen()
        pencil.setWidth(3)
        pencil.setColor(QtGui.QColor(160 ,160, 160, 155))
        object.setPen(pencil)
        object.drawLine(x1, y1, x2, y2)

        
class OptionsGame(QtGui.QDialog):
    """
    Class with options' window.
    """
    
    def __init__(self):
        super(OptionsGame, self).__init__()
        
        self.initUI()
        self.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
        SudokuMainWindow.changeOptions = False

        self.reset = False
    
    def initUI(self):      
        
        # checked
        self.col0 = SudokuMainWindow.colorCheck
        self.col = SudokuMainWindow.colorCheck

        self.btn = QtGui.QPushButton('Change color checked cell', self)
        self.btn.move(20, 60)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QtGui.QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % self.col.name())
        self.frm.setGeometry(250, 22, 100, 100)  
        
        # solved
        self.col20 = SudokuMainWindow.colorSolve
        self.col2 = SudokuMainWindow.colorSolve
        
        self.btn2 = QtGui.QPushButton('Change color solved cell', self)
        self.btn2.move(20, 232)

        self.btn2.clicked.connect(self.showDialog2)
        self.frm2 = QtGui.QFrame(self)
        self.frm2.setStyleSheet("QWidget { background-color: %s }" 
            % self.col2.name())
        self.frm2.setGeometry(250, 202, 100, 100) 
        
        self.qbtn = QtGui.QPushButton('OK', self)
        self.rbtn = QtGui.QPushButton('Reset', self)
        self.cbtn = QtGui.QPushButton('Cancel', self)
        self.connect(self.qbtn, QtCore.SIGNAL('clicked()'), self.changeColor)
        self.connect(self.qbtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('accept()'))
        self.connect(self.rbtn, QtCore.SIGNAL('clicked()'), self.resetColor)
        self.connect(self.cbtn, QtCore.SIGNAL('clicked()'), self.cancelColor)
        self.connect(self.cbtn, QtCore.SIGNAL('clicked()'), QtCore.SLOT('accept()'))
        self.qbtn.resize(self.qbtn.sizeHint())
        self.rbtn.resize(self.qbtn.sizeHint())
        self.cbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(60, 350)
        self.rbtn.move(160, 350)
        self.cbtn.move(260, 350)
        
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Options game')
        self.show()
        
    def changeColor(self):
        """
        zmiana koloru okienek sprawdzonych i zle wypelnionych
        """
        if not self.reset:
            SudokuMainWindow.colorCheck = self.col
            SudokuMainWindow.colorSolve = self.col2
        if self.reset:
            SudokuMainWindow.colorCheck = SudokuMainWindow.colorCheck0
            SudokuMainWindow.colorSolve = SudokuMainWindow.colorSolve0
        
    def resetColor(self):
        """
        przywrocenie pierwotnych kolorow okienek
        """
        self.reset = True
        
        SudokuMainWindow.changeOptions = True
        
        if self.col == SudokuMainWindow.colorCheck0 and self.col2 == SudokuMainWindow.colorSolve0:
            SudokuMainWindow.changeOptions = False      

        self.col = SudokuMainWindow.colorCheck0
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                % self.col.name())

        self.col2 = SudokuMainWindow.colorSolve0
        self.frm2.setStyleSheet("QWidget { background-color: %s }"
                % self.col2.name())
                
        if self.col == SudokuMainWindow.colorCheck and self.col2 == SudokuMainWindow.colorSolve:
            SudokuMainWindow.changeOptions = False
        
    def cancelColor(self):
        """
        powrot do poprzednich ustawień
        """
        if self.reset:
            self.col = SudokuMainWindow.colorCheck
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % self.col.name())
            self.col2 = SudokuMainWindow.colorSolve
            self.frm2.setStyleSheet("QWidget { background-color: %s }"
                % self.col2.name())
        SudokuMainWindow.changeOptions = False
            
        
        
    def showDialog(self, col):
      
        self.col = QtGui.QColorDialog.getColor()

        if self.col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % self.col.name())
        notice = NoticeWindow()
        notice.exec_()
        SudokuMainWindow.changeOptions = True
            
    def showDialog2(self, col):
      
        self.col2 = QtGui.QColorDialog.getColor()

        if self.col2.isValid():
            self.frm2.setStyleSheet("QWidget { background-color: %s }"
                % self.col2.name())
        notice = NoticeWindow()
        notice.exec_()
        SudokuMainWindow.changeOptions = True
        
class NoticeWindow(QtGui.QDialog):
    """
    klasa odpowiedzialna, za pojawiania się okna
    po nacisnieciu przycisku 'Check'
    """
    def __init__(self, checkbool = True, end = False):
        super(NoticeWindow, self).__init__()
        self.setWindowTitle('Options Notice')
        self.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
        
        check = QtGui.QWidget(self)
        x = "After changing color, your SuDoKu game will be restarted to apply new setting!"
        label = QtGui.QLabel(x)
 
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label, 0, QtCore.Qt.AlignCenter)
        check.setLayout(layout)
        
        okbutton = QtGui.QPushButton('&OK')
        self.connect(okbutton, QtCore.SIGNAL('clicked()'), self, QtCore.SLOT('accept()'))
            
        
        bbox = QtGui.QHBoxLayout()
        bbox.addStretch()
        bbox.addWidget(okbutton)
        bbox.addStretch()
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(check)
        layout.addLayout(bbox)
        self.setLayout(layout)