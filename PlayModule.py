import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui, QtMultimedia
from functools import partial


class PlayWidget(QtWidgets.QWidget):
    def __init__(self, operation_selection, parent=None):
        super(PlayWidget, self).__init__(parent)

        sound = QtMultimedia.QSound("sounds/blip2.wav")
        sound.play()

        self.operand = operation_selection
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
        self.QuestionLayout.setAlignment(QtCore.Qt.AlignCenter)

        #   input section
        self.TextInput = QtWidgets.QLineEdit()
        self.TextInput.setAlignment(QtCore.Qt.AlignCenter)
        self.TextInput.setStyleSheet("color: white; padding: 30px 0px; font-size: 35px;")
        self.TextInput.returnPressed.connect(self.operate)
        self.submitButton = QtWidgets.QPushButton("Submit")
        self.submitButton.setStyleSheet("background-color: green; color: white; padding: 15px 15px; font-size: 20px; border-radius: 10px;")

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
            [QtWidgets.QPushButton('+/-'), QtWidgets.QPushButton('0'), QtWidgets.QPushButton('DEL')]]
        for i in range(0,4):
            for j in range(0, 3):
                self.numPadButtons[i][j].clicked.connect(partial(self.enterNumber, self.numPadButtons[i][j].text()))
        for i in range(0, 4):
            for j in range(0, 3):
                self.numPadButtons[i][j].setStyleSheet("background-color: #002993; color: #FFFFFF; padding: 20px 20px; font-size: 35px; border-radius: 20px;")
                self.inputLayout.addWidget(self.numPadButtons[i][j], i+1, j)
        self.inputLayout.setVerticalSpacing(20)

        #   layout all widgets
        self.stack = QtWidgets.QVBoxLayout()
        self.stack.addLayout(self.QuestionLayout)
        self.stack.addLayout(self.inputLayout)
        self.setLayout(self.stack)

        self.shuffle() #Shuffle here to make sure that the operands are valid using shuffle's error checking
    
    def enterNumber(self, txt):
        if (txt == "+/-"):
            #Change sign
            temp_text = self.TextInput.text()
            if (len(temp_text) > 0):
                if( temp_text[0] == '-' ):
                    self.TextInput.setText(temp_text[1:len(temp_text)])
                else:
                    self.TextInput.setText('-' + temp_text)
        elif (txt == 'DEL'):
            #Delete character
            temp_text = self.TextInput.text()
            self.TextInput.setText("" if (len(temp_text) == 0) else temp_text[0:-1])
        else:
            self.TextInput.setText(self.TextInput.text() + txt)
        
    def shuffle(self):
        right = random.choice(self.random)
        left = random.choice(self.random)

        if self.operand == '-':
            if int(right) > int(left):
                temp = right
                right = left
                left = temp
        elif self.operand == '/':
            temp_res = int(left) / int(right)
            if int(temp_res) != temp_res: #Not an integer result,
                left = str(int(left)*int(right))

        self.numLeft.setText(left)
        self.numRight.setText(right)
        self.numLeft.repaint()
        self.numRight.repaint()
    
    def operate(self):
        wrong = False
        try:
            if(self.operand == "+"):
                wrong = (int(self.numLeft.text()) + int(self.numRight.text())) != int(self.TextInput.text())
            elif(self.operand == "-"):
                wrong = (int(self.numLeft.text()) - int(self.numRight.text())) != int(self.TextInput.text())
            elif(self.operand == "*"):
                wrong = (int(self.numLeft.text()) * int(self.numRight.text())) != int(self.TextInput.text())
            elif(self.operand == "/"):
                wrong = (int(int(self.numLeft.text()) / int(self.numRight.text()))) != int(self.TextInput.text())
        except ValueError:
            sound = QtMultimedia.QSound("sounds/wrong.wav")
            sound.play()
            self.showMessageBox("Invalid input. Please use numerical characters to input integers.")
            return
        
        if(wrong):
            sound = QtMultimedia.QSound("sounds/wrong.wav")
            sound.play()
            self.showMessageBox("Incorrect, please try again.")
        else:
            sound = QtMultimedia.QSound("sounds/correct.wav")
            sound.play()
            self.showMessageBox("Nice job! You got it!")
            self.TextInput.clear()
            self.shuffle()
            
            

    def showMessageBox(self, value):
        #QtWidgets.QMessageBox.information(self, "Scales", value)

        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Scales")
        msgBox.setText(value)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        if( len(value) >= 9 ):
            if (value[0:9] == "Nice job!"):
                QtWidgets.QMessageBox.setStyleSheet(msgBox, "background-color: green; color: white")
            elif (value[0:9] == "Incorrect" or value[0:7] == "Invalid"):
                QtWidgets.QMessageBox.setStyleSheet(msgBox, "background-color: red; color: white")
            else:
                QtWidgets.QMessageBox.setStyleSheet(msgBox, "background-color: white; color: black")
        else:
            QtWidgets.QMessageBox.setStyleSheet(msgBox, "background-color: white; color: black")
            print("Invalid value passed, choose something which starts with 'Incorrect' or 'Nice Job!'")
        msgBox.exec()
