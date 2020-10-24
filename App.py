import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class PlayWidget(QtWidgets.QWidget):
    def __init__(self, operand):
        super().__init__()

        self.operand = operand
        self.random = ['1','2','3','4','5','6','7','8','9','10']

        textStyle = ("color: white; font-size: 30px;")
        solStyle = ("color: red; font-size: 35px;")

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
        #  apply layout
        #self.setLayout(self.QuestionLayout)

        self.TextInput = QtWidgets.QLineEdit()
        self.TextInput.setStyleSheet("color: white; padding: 30px 0px; font-size: 35px;")
        self.TextInput.returnPressed.connect(self.operate)
        self.submitButton = QtWidgets.QPushButton("Submit")
        self.submitButton.setStyleSheet("background-color: green; color: white; padding: 15px 15px; font-size: 20px; border-radius: 10px;")

        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.addWidget(self.TextInput)
        self.inputLayout.addWidget(self.submitButton)
        self.submitButton.clicked.connect(self.operate)
        #self.setLayout(self.inputLayout)


        self.stack = QtWidgets.QVBoxLayout()
        self.stack.addLayout(self.QuestionLayout)
        self.stack.addLayout(self.inputLayout)
        self.setLayout(self.stack)
    
    def shuffle(self):
        self.numLeft.setText(random.choice(self.random))
        self.numRight.setText(random.choice(self.random))
        self.numLeft.repaint()
        self.numRight.repaint()
    
    def operate(self):
        if(self.operand == "+"):
            if ((int(self.numLeft.text()) + int(self.numRight.text())) != int(self.TextInput.text())):
                print("rip")
                self.showMessageBox("Incorrect, please try again.")
            else:
                print("nice")
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()
        elif(self.operand == "-"):
            if ((int(self.numLeft.text()) - int(self.numRight.text())) != int(self.TextInput.text())):
                print("rip")
                self.showMessageBox("Incorrect, please try again.")
            else:
                print("nice")
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()
        elif(self.operand == "*"):
            if ((int(self.numLeft.text()) * int(self.numRight.text())) != int(self.TextInput.text())):
                print("rip")
                self.showMessageBox("Incorrect, please try again.")
            else:
                print("nice")
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()
        elif(self.operand == "/"):
            if ((int(self.numLeft.text()) / int(self.numRight.text())) != int(self.TextInput.text())):
                print("rip")
                self.showMessageBox("Incorrect, please try again.")
            else:
                print("nice")
                self.showMessageBox("Nice job! you got it!")
                self.TextInput.clear()
                self.shuffle()

    def showMessageBox(self, value):
        QtWidgets.QMessageBox.information(self, "Scales", value)


        


class HomeWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

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

        self.learnButton.clicked.connect(self.learnButtonClicked)
        self.playButton.clicked.connect(self.playButtonClicked)
        #self.button.clicked.connect(self.magic)
    def learnButtonClicked(self):
        print('learn')

    def playButtonClicked(self):
        print('play')
    #def magic(self):
        #self.text.setText(random.choice(self.hello))
        #self.text.repaint()

if __name__ == "__main__":
  app = QtWidgets.QApplication([])
  widget = PlayWidget('-')
  widget.setStyleSheet("background-color: rgb(39,71,133);")
  widget.resize(800,600)
  widget.show()

  sys.exit(app.exec_())
