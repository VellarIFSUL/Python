#importar bibliotecas:
from PyQt5 import uic,QtWidgets


#Função 1
def GetText():
    Num = janela.LineEdit.text()
    Num = Num.split(" ")
    return Num

#Função 2
def SetTxt(i):
    janela.Resultado.setText(str(i))

#Função 3
def somar(N):
    S = 0
    for i in N:
        try:
            S+=int(i)
        except:
            S+=0
    return S

#Função Principal Chamada no clicar do botão
def Executar():
    S = somar(GetText())
    SetTxt(S)


#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("funcoes.ui")
janela.BtnSoma.clicked.connect(Executar)
janela.show()
app.exec()