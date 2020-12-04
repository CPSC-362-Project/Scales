import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from functools import partial


class LearnWidget(QtWidgets.QWidget):
    def __init__(self, operation_selection, parent=None):
        super(LearnWidget, self).__init__(parent)

        operand = operation_selection
        self.learnMul = ["Welcome to Scales!", "Let's start with multiplying.", "We can use our fingers \n to multiply numbers.", "Lets multiply 2 and 3.", "Put up 3 fingers", "Now add 3 more fingers", "We have added 3 fingers \n two times!", "This is the same as\n multiplying two numbers!", "How many fingers\n do you have up?", "6! Did you get it right?", "Click back to \n pick another \n module."]
        self.learnDiv = ["Welcome to Scales!", "Let's start with dividing.", "We can use our fingers to\n divide numbers.", "Lets divide 6 by 3.", "Put up 6 fingers.", "Take down fingers\n 3 at a time.", "How many fingers\n did you take away\n before you go to 0?", "That's the answer to 6/3!", "Did you answer 2?", "If so, you got it right!", "Click back to \n pick another \n module."]
        self.learnSub = ["Welcome to Scales!", "Let's start with subtracting.", "We can use our fingers \n to subtract numbers.", "Lets subtract 5 from 2.", "Put up 5 fingers.", "Take down 2.", "How many fingers are left?", "3! Did you get it right?", "Click back to \n pick another \n module."]
        self.learnTexts = ["Welcome to Scales!", "Let's start with adding.", "We can use our fingers\n to add numbers.", "Let's add 3 and 2.", "Lets put up 3 fingers.", "Now count 2 more.", "How many fingers are up?", "5! Did you get it right?", "Click back to \n pick another \n module."]

        self.tutorial = []
        if operand == "+":
            self.tutorial = self.learnTexts
        elif operand == "-":
            self.tutorial = self.learnSub
        elif operand == "*":
            self.tutorial = self.learnMul
        elif operand == "/":
            self.tutorial = self.learnDiv

        self.currentText = 0
        

        # Snakey Image
        self.snakeCartoon = QtWidgets.QLabel()
        snakepng = QtGui.QPixmap('images/snake1.png')
        snakeScaled = snakepng.scaled(450, 450, QtCore.Qt.KeepAspectRatio)
        self.snakeCartoon.setPixmap(snakeScaled)

        # Tutorial Text
        self.tutorialText = QtWidgets.QLabel(self.tutorial[self.currentText])
        self.tutorialText.setStyleSheet("color: white; font-size: 52px;")
        self.tutorialText.adjustSize()
        self.tutorialText.wordWrap()

        # Tutorial Navigation Stuff
        navStyle = ("color: white; font-size: 22px; margin: 0 15px")
        self.nextButton = QtWidgets.QPushButton("Next")
        self.backButton = QtWidgets.QPushButton("Back")
        self.nextButton.setStyleSheet(navStyle)
        self.backButton.setStyleSheet(navStyle)
        self.nextButton.clicked.connect(self.next)
        self.backButton.clicked.connect(self.back)

        # horizontal Layout for side by side buttons
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.nextButton)

        # Veritcal Layout - right side of page
        self.vertLayout = QtWidgets.QVBoxLayout()
        self.vertLayout.addWidget(self.tutorialText)
        self.vertLayout.addLayout(self.buttonLayout)

        # Horizontal Layout
        self.splitLayout = QtWidgets.QHBoxLayout()
        self.splitLayout.addWidget(self.snakeCartoon)
        self.splitLayout.addLayout(self.vertLayout)
        self.splitLayout.setAlignment(QtCore.Qt.AlignCenter)


        # Apply the layout
        self.setLayout(self.splitLayout)

    def next(self):
        if self.currentText + 1 < len(self.tutorial):
            self.currentText += 1
            self.tutorialText.setText(self.tutorial[self.currentText])
            self.tutorialText.repaint()
    
    def back(self):
        if self.currentText > 0:
            self.currentText -= 1
            self.tutorialText.setText(self.tutorial[self.currentText])
            self.tutorialText.repaint()

