# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Luis\Desktop\python\Sql\telaListaCategoria.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcluir.setGeometry(QtCore.QRect(10, 370, 91, 41))
        self.btnExcluir.setStyleSheet("font-size:20px;\n"
"background-color:red;")
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnCad = QtWidgets.QPushButton(self.centralwidget)
        self.btnCad.setGeometry(QtCore.QRect(180, 370, 101, 41))
        self.btnCad.setStyleSheet("font-size:20px;\n"
"background-color:yellow;")
        self.btnCad.setObjectName("btnCad")
        self.btnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditar.setGeometry(QtCore.QRect(340, 370, 91, 41))
        self.btnEditar.setStyleSheet("font-size:20px;\n"
"background-color:cyan;")
        self.btnEditar.setObjectName("btnEditar")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 421, 351))
        self.tableWidget.setStyleSheet("background-color:white")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(127)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnExcluir.setText(_translate("MainWindow", "Excluir"))
        self.btnCad.setText(_translate("MainWindow", "Cadastrar"))
        self.btnEditar.setText(_translate("MainWindow", "Editar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
