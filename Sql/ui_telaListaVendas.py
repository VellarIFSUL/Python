# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Luis\Desktop\python\Sql\telaListaVendas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 477)
        MainWindow.setStyleSheet("background-color:grey;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCad = QtWidgets.QPushButton(self.centralwidget)
        self.btnCad.setGeometry(QtCore.QRect(460, 380, 101, 41))
        self.btnCad.setStyleSheet("font-size:20px;\n"
"background-color:yellow;")
        self.btnCad.setObjectName("btnCad")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 551, 351))
        self.tableWidget.setStyleSheet("background-color:white")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)
        self.btnPDF = QtWidgets.QPushButton(self.centralwidget)
        self.btnPDF.setGeometry(QtCore.QRect(240, 380, 91, 41))
        self.btnPDF.setStyleSheet("font-size:20px;\n"
"background-color:blue;")
        self.btnPDF.setObjectName("btnPDF")
        self.btnExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcluir.setGeometry(QtCore.QRect(10, 380, 91, 41))
        self.btnExcluir.setStyleSheet("font-size:20px;\n"
"background-color:red;")
        self.btnExcluir.setObjectName("btnExcluir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
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
        self.btnCad.setText(_translate("MainWindow", "Cadastrar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Produto"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Qtd."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Preço"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total"))
        self.btnPDF.setText(_translate("MainWindow", "PDF"))
        self.btnExcluir.setText(_translate("MainWindow", "Excluir"))