import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from functools import partial
import LearnModule as Learn
import PlayModule as Play


class HomeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)

        self.learnButton = QtWidgets.QPushButton("Learn")
        self.learnButton.setStyleSheet("color: green; background-color: rgb(59,48,57); height: 100px; width: 200px; font-size: 45px; border-radius: 20px;")
        self.playButton = QtWidgets.QPushButton("Play")
        self.playButton.setStyleSheet("color: green; background-color: rgb(59,48,57); height: 100px; width: 200px; font-size: 45px; border-radius: 20px;")
        self.title = QtWidgets.QLabel("Scales")
        self.title.setStyleSheet("font-size: 100px; color: green;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.learnButton)
        self.layout.addWidget(self.playButton)
        self.setLayout(self.layout)


class ModuleSelectorWidget(QtWidgets.QWidget):
    def __init__(self, modType, parent=HomeWidget):
        super(ModuleSelectorWidget, self).__init__(parent)
        self.parent = parent
        self.modType = modType
        self.selectionGrid = QtWidgets.QGridLayout()
        self.operation_selections = [[QtWidgets.QPushButton("+"), QtWidgets.QPushButton("-")],
            [QtWidgets.QPushButton("*"), QtWidgets.QPushButton("/")]] 

        option_colors = [['#d14590', '#c24a32'], ['#315dbd', '#c7a336']]

        self.selectionGrid = QtWidgets.QGridLayout()
        for i in range(0,2):
            for j in range(0,2):
                temp_button = self.operation_selections[i][j]
                temp_button.setStyleSheet("background-color: " + option_colors[i][j] + "; color: #FFFFFF; margin: 10% 80%; font-size: 50px; border-radius: 15px")
                temp_button.clicked.connect(partial(self.select, temp_button.text()))
                self.selectionGrid.addWidget(temp_button, i, j)

        self.operation_selections[0][0].setText("\n+\n\nAddition\n")
        self.operation_selections[0][1].setText("\n-\n\nSubtraction\n")
        self.operation_selections[1][0].setText("\n×\n\nMultiplication\n")
        self.operation_selections[1][1].setText("\n÷\n\nDivision\n")

        self.stack = QtWidgets.QVBoxLayout()
        #self.stack.addLayout(self.QuestionLayout)
        #self.stack.addLayout(self.inputLayout)
        self.stack.addLayout(self.selectionGrid)
        self.setLayout(self.stack)
    
    def select(self, op_string):
        temp_str = ""
        if(op_string == "+"):
            temp_str = "Addition"
        elif (op_string == "-"):
            temp_str = "Subtraction"
        elif (op_string == "*"):
            temp_str = "Multiplication"
        elif (op_string == "/"):
            temp_str = "Division"
            
        if (self.modType == "Learn"):
            self.parent.LearnWidget = Learn.LearnWidget(op_string, self.parent)
            self.parent.setWindowTitle("Scales - Learn: " + temp_str)
            self.parent.setCentralWidget(self.parent.LearnWidget)
        elif (self.modType == "Play"):
            self.parent.PlayWidget = Play.PlayWidget(op_string, self.parent)
            self.parent.setWindowTitle("Scales - Play: " + temp_str)
            self.parent.setCentralWidget(self.parent.PlayWidget)

        else:
            print("Type must be \"Learn\" or \"Play\"")
    
        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.ToolBar = self.addToolBar("Back")
        
        self.back_action = QtWidgets.QAction("Back", self)
        self.back_action.setStatusTip("Go back")
        self.back_action.triggered.connect(partial(self.backAction))
        self.ToolBar.addAction(self.back_action)
        self.ToolBar.setMovable(False)
        self.ToolBar.setStyleSheet("color: white;")
        #self.setFixedSize(400, 450)
        self.startHomeWidget()

    def startHomeWidget(self):
        self.HomeWidget = HomeWidget(self)
        self.setWindowTitle("Scales - Home")
        self.setCentralWidget(self.HomeWidget)
        self.HomeWidget.playButton.clicked.connect(self.startPlayWidget)
        self.HomeWidget.learnButton.clicked.connect(self.startLearnWidget)
        self.ToolBar.setVisible(False)
        self.show()

    def startLearnWidget(self):
        self.SelectWidget = ModuleSelectorWidget("Learn", self)
        self.setWindowTitle("Scales - Learn: Select")
        self.setCentralWidget(self.SelectWidget)
        self.ToolBar.setVisible(True)
        self.show()
        
    def startPlayWidget(self):
        self.SelectWidget = ModuleSelectorWidget("Play", self)
        self.setWindowTitle("Scales - Play: Select")
        self.setCentralWidget(self.SelectWidget)
        self.ToolBar.setVisible(True)
        self.show()

    def backAction(self):
        curr_class = str(type(self.centralWidget()))
        #print(curr_class) #For Debugging Purposes
        if (curr_class == "<class 'PlayModule.PlayWidget'>"):
            self.startPlayWidget()
        elif (curr_class == "<class 'LearnModule.LearnWidget'>"):
            self.startLearnWidget()
        else: #Default to main menu
            self.startHomeWidget()


if __name__ == "__main__":
    
  app = QtWidgets.QApplication([])
  #widget = PlayWidget('-')
  widget = MainWindow()
  widget.setStyleSheet("background-color: rgb(39,71,133);")
  widget.resize(1000,800)
  widget.show()

  sys.exit(app.exec_())
