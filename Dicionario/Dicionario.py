#importar bibliotecas:
from tokenize import String
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

dicio=dict()

def adicionar():
    nome=janela.Nome.text()
    idade=janela.Idade.value()
    if nome!="":
        janela.Nome.clear()
        janela.Idade.setValue(1)
        dicio[nome]=idade
    else:
        QMessageBox.critical(janela, "Error", "Nenhum nome no campo!", QMessageBox.Yes)

def listar():
    for nome in dicio.keys():
        janela.List.addItem(nome+" - "+str(dicio[nome]))

#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("Dicionario.ui")

janela.Adicionar.clicked.connect(adicionar)
janela.ListarDados.clicked.connect(listar)

janela.show()
app.exec()