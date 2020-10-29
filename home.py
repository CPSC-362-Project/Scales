# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 709)
        MainWindow.setStyleSheet("background-color: rgb(39,71,133);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.HomePageWidget = QtWidgets.QWidget(MainWindow)
        self.HomePageWidget.setAutoFillBackground(False)
        self.HomePageWidget.setObjectName("HomePageWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.HomePageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.HomePageWidget)
        font = QtGui.QFont()
        font.setFamily("OCR A Std")
        font.setPointSize(55)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(237,180,56);\n"
"font: 55pt \"OCR A Std\";\n"
"")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(45, 45, 45, 45)
        self.horizontalLayout.setSpacing(45)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.HomePageWidget)
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QtCore.QSize(400, 270))
        self.widget.setMaximumSize(QtCore.QSize(400, 270))
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.widget.setStyleSheet("background-color: rgb(59,48,57);\n"
"border-radius: 20px;\n"
"cursor: pointer;\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("color: white;\n"
"font-size: 150px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.HomePageWidget)
        self.widget_2.setMinimumSize(QtCore.QSize(400, 270))
        self.widget_2.setMaximumSize(QtCore.QSize(400, 270))
        self.widget_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.widget_2.setStyleSheet("background-color: rgb(59,48,57);\n"
"border-radius: 20px;\n"
"cursor: pointer;\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 9, 471, 231))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setStyleSheet("color: white;\n"
"font-size: 130px;\n"
"")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.HomePageWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scales"))
        self.label.setText(_translate("MainWindow", "Scales"))
        self.label_2.setText(_translate("MainWindow", "Play"))
        self.label_5.setText(_translate("MainWindow", "Learn"))