#importar bibliotecas:
from tokenize import String
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

dicio=dict()

def adicionar():
    nome=janela.Nome.text()
    idade=janela.Idade.value()
    continua=True
    for i in range(janela.filtro.count()):
        if(str(idade)==janela.filtro.itemText(i)):
            continua=False
    if(continua):
        janela.filtro.addItem(str(idade))
    if nome!="":
        janela.Nome.clear()
        janela.Idade.setValue(1)
        dicio[nome]=idade
    else:
        QMessageBox.critical(janela, "Error", "Nenhum nome no campo!", QMessageBox.Yes)

def listar():
    janela.List.clear()
    filtro=janela.filtro.currentText()
    for nome in dicio.keys():
        if(filtro!='Filtro'):
            if(filtro==str(dicio[nome])):
                janela.List.addItem(nome+" - "+str(dicio[nome]))
        else:
            janela.List.addItem(nome+" - "+str(dicio[nome]))


#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("Dicionario.ui")

janela.Adicionar.clicked.connect(adicionar)
janela.ListarDados.clicked.connect(listar)

janela.show()
app.exec()