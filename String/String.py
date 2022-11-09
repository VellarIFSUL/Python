#importar bibliotecas:
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

def GetText():
    return janela.Input.text()

def SetTxt(inp):
    janela.LblResult.setText(inp)

def AllCaps():
    str = GetText()
    SetTxt(str.upper())

def Lower():
    str = GetText()
    SetTxt(str.lower())

def Capitalize():
    str = GetText()
    SetTxt(str.capitalize())

def BeginEnd():
    str = GetText()
    str = str.split(" ")
    if(len(str)<=1):
        str=str[0]
    else:
        str=str[0]+" "+str[len(str)-1]
    SetTxt(str)

def StringIn():
    str = GetText()
    if('A' in str):
        SetTxt("'"+str+"' possui 'A'")
    else:
        SetTxt("'"+str+"' não possui 'A'")

#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("String.ui")

janela.BtnAllCaps.clicked.connect(AllCaps)
janela.BtnCapitalize.clicked.connect(Capitalize)
janela.BtnLower.clicked.connect(Lower)
janela.BtnBgEnd.clicked.connect(BeginEnd)
janela.BtnIn.clicked.connect(StringIn)

janela.show()
app.exec()