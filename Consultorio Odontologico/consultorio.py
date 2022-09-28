#importar bibliotecas:
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

pacientes = []

def adiciona():
    nome=janela.LblNome.text()
    if nome!="":
        janela.LblNome.clear()
        pacientes.append(nome) #adiciona no vetor
        janela.LblPac.addItem(nome)
    else:
        QMessageBox.critical(janela, "Error", "Nenhum nome no campo!", QMessageBox.Yes)

def limpar():
    janela.LblPac.clear()
    janela.LblAt.clear()

def mostra_dados():
    tam = len(pacientes) #lê o tamanho do vetor
    for i in range(tam):
        janela.LblPac.addItem(pacientes[i])

def fechar():
    sair = QMessageBox.question(janela, "Saindo do sistema", "Deseja mesmo sair do sistema?", QMessageBox.Yes, QMessageBox.No)
    if sair == QMessageBox.Yes:
        janela.close()

def transferir():
    if janela.LblAt.count()<1:
        temp = janela.LblPac.currentItem().text()
        janela.LblPac.takeItem(janela.LblPac.currentRow())
        janela.LblAt.addItem(temp)

#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("consultorio.ui")

janela.BtnAdc.clicked.connect(adiciona)
janela.BtnLimpar.clicked.connect(limpar)
janela.BtnMostrar.clicked.connect(mostra_dados)
janela.BtnFechar.clicked.connect(fechar)
janela.BtnPass.clicked.connect(transferir)

janela.show()
app.exec()