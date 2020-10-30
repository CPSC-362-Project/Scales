import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

"""
class ModuleSelectorWidget(QtWidgets.QWidget):
    def __init__(self, parent=HomeWidget):
        super(ModuleSelectorWidget, self).__init__(parent)
        """

class PlayWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PlayWidget, self).__init__(parent)

        self.operand = '-'
        self.random = ['1','2','3','4','5','6','7','8','9','10']

        textStyle = ("color: white; font-size: 60px;")
        solStyle = ("color: red; font-size: 65px;")

        # question widget
        self.numLeft = QtWidgets.QLabel(random.choice(self.random))
        self.op = QtWidgets.QLabel(self.operand)
        self.numRight = QtWidgets.QLabel(random.choice(self.random))
        self.eq = QtWidgets.QLabel("=")
        self.sol = QtWidgets.QLabel("?")

        self.numLeft.setStyleSheet(textStyle)
        self.op.setStyleSheet(textStyle)
        self.numRight.setStyleSheet(textStyle)
        self.eq.setStyleSheet(textStyle)
        self.sol.setStyleSheet(solStyle)

        # question layout
        self.QuestionLayout = QtWidgets.QHBoxLayout()
        self.QuestionLayout.addWidget(self.numLeft)
        self.QuestionLayout.addWidget(self.op)
        self.QuestionLayout.addWidget(self.numRight)
        self.QuestionLayout.addWidget(self.eq)
        self.QuestionLayout.addWidget(self.sol)

        #   input section
        self.TextInput = QtWidgets.QLineEdit()
        self.TextInput.setStyleSheet("color: white; padding: 30px 0px; font-size: 35px;")
        self.TextInput.returnPressed.connect(self.operate)
        self.submitButton = QtWidgets.QPushButton("Submit")
        self.submitButton.setStyleSheet("background-color: green; color: white; padding: 15px 15px; font-size: 20px; border-radius: 10px;")

        '''
        #   input layout
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.addWidget(self.TextInput)
        self.inputLayout.addWidget(self.submitButton)
        self.submitButton.clicked.connect(self.operate)
        '''
        #   numpad input layout
        self.inputLayout = QtWidgets.QGridLayout()
        #self.inputLayout.setStyleSheet("background-color: #FFFFFF; opacity: 0.2; border-radius: 5px; border-color: black") #Style for numpad background
        self.inputLayout.addWidget(self.TextInput, 0,0, 1,2)
        self.inputLayout.addWidget(self.submitButton, 0,2)
        self.submitButton.clicked.connect(self.operate)

        self.numPadButtons = [
            [QtWidgets.QPushButton('7'), QtWidgets.QPushButton('8'), QtWidgets.QPushButton('9')], 
            [QtWidgets.QPushButton('4'), QtWidgets.QPushButton('5'), QtWidgets.QPushButton('6')], 
            [QtWidgets.QPushButton('1'), QtWidgets.QPushButton('2'), QtWidgets.QPushButton('3')], 
            [QtWidgets.QPushButton('-'), QtWidgets.QPushButton('0'), QtWidgets.QPushButton('DEL')]]

        for i in range(0, 4):
            for j in range(0, 3):
                self.numPadButtons[i][j].setStyleSheet("background-color: #002993; color: #FFFFFF")
                self.inputLayout.addWidget(self.numPadButtons[i][j], i+1, j)

        self.inputLayout.setVerticalSpacing(20)

        #   layout all widgets
        self.stack = QtWidgets.QVBoxLayout()
        self.stack.addLayout(self.QuestionLayout)
        self.stack.addLayout(self.inputLayout)
        self.setLayout(self.stack)
    
    def shuffle(self):

        right = random.choice(self.random)
        left = random.choice(self.random)

        if self.operand == '-':
            if int(right) > int(left):
                temp = right
                right = left
                left = temp

        self.numLeft.setText(left)
        self.numRight.setText(right)
        self.numLeft.repaint()
        self.numRight.repaint()
    
    def operate(self):
        if(self.operand == "+"):
            if ((int(self.numLeft.text()) + int(self.numRight.text())) != int(self.TextInput.text())):
                self.showMessageBox("Incorrect, please try again.")
            else:
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()
        elif(self.operand == "-"):
            if ((int(self.numLeft.text()) - int(self.numRight.text())) != int(self.TextInput.text())):
                self.showMessageBox("Incorrect, please try again.")
            else:
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()
        elif(self.operand == "*"):
            if ((int(self.numLeft.text()) * int(self.numRight.text())) != int(self.TextInput.text())):
                self.showMessageBox("Incorrect, please try again.")
            else:
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()
        elif(self.operand == "/"):
            if ((int(self.numLeft.text()) / int(self.numRight.text())) != int(self.TextInput.text())):
                self.showMessageBox("Incorrect, please try again.")
            else:
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()

    def showMessageBox(self, value):
        QtWidgets.QMessageBox.information(self, "Scales", value)


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



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        #self.setFixedSize(400, 450)
        self.startHomeWidget()

    def startHomeWidget(self):
        self.HomeWidget = HomeWidget(self)
        self.setWindowTitle("Scales - Home")
        self.setCentralWidget(self.HomeWidget)
        self.HomeWidget.playButton.clicked.connect(self.startPlayWidget)
        self.show()

    def startPlayWidget(self):
        self.PlayWidget = PlayWidget(self)
        self.setWindowTitle("Scales - Play")
        self.setCentralWidget(self.PlayWidget)
        self.show()


if __name__ == "__main__":
    
  app = QtWidgets.QApplication([])
  #widget = PlayWidget('-')
  widget = MainWindow()
  widget.setStyleSheet("background-color: rgb(39,71,133);")
  widget.resize(1000,800)
  widget.show()

  sys.exit(app.exec_())
