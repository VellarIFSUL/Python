# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Luis\Desktop\python\Funcoes\funcoes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 249)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BtnSoma = QtWidgets.QPushButton(self.centralwidget)
        self.BtnSoma.setGeometry(QtCore.QRect(150, 70, 91, 23))
        self.BtnSoma.setObjectName("BtnSoma")
        self.LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.LineEdit.setGeometry(QtCore.QRect(50, 30, 311, 20))
        self.LineEdit.setObjectName("LineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 100, 171, 41))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.Resultado = QtWidgets.QLabel(self.centralwidget)
        self.Resultado.setGeometry(QtCore.QRect(150, 150, 91, 41))
        self.Resultado.setText("")
        self.Resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.Resultado.setObjectName("Resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Funcoes"))
        self.BtnSoma.setText(_translate("MainWindow", "Somar Numeros"))
        self.label.setText(_translate("MainWindow", "Separe os numeros por um espaço"))