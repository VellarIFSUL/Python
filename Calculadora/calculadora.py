#importar bibliotecas:
from cmath import sqrt
from tokenize import Double, String
from xml.etree.ElementTree import tostring
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

def Calcula():
    Certo = True
    N1 = janela.LblN1.text()
    N2 = janela.LblN2.text()

    try:
        N1 = float(N1)
    except:
        Limpa()
        Certo = False
        QMessageBox.critical(janela, "Erro", "Erro!! no 1º Numero")
    
    if not janela.Rb6.isChecked():
        try:
            N2 = float(N2)
        except:
            Limpa()
            Certo = False
            QMessageBox.critical(janela, "Erro", "Erro!! no 2º Numero")

    if Certo:
        try:
            if janela.Rb1.isChecked():
                Res=N1+N2
            elif janela.Rb2.isChecked():
                Res=N1-N2
            elif janela.Rb3.isChecked():
                Res=N1*N2
            elif janela.Rb4.isChecked():
                Res=N1/N2
            elif janela.Rb5.isChecked():
                Res=N1**N2
            elif janela.Rb6.isChecked():
                Res=sqrt(N1)
        except:
            Limpa()
            QMessageBox.critical(janela, "Erro", "Ops Algo deu Errado :(")
        else:
            janela.LblResultado.setText(str(Res))


def Limpa():
    janela.LblN1.setText("")
    janela.LblN2.setText("")
    janela.LblResultado.setText("")

def Sai():
    result = QMessageBox.question(janela, "Saindo do sistema", "Deseja mesmo sair do sistema?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()

#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("calculadora.ui")

janela.BtnCalcula.clicked.connect(Calcula)
janela.BtnLimpa.clicked.connect(Limpa)
janela.BtnSai.clicked.connect(Sai)

janela.show()
app.exec()