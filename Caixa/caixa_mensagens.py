#importar bibliotecas:
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

def fechar_tela():
    result = QMessageBox.question(janela, "Saindo do sistema", "Deseja mesmo sair do sistema?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()

def listar_dados():
    #Nome
    dado_lido = janela.LeNome.text()

    #Confere Nome se n estiver vazio
    if dado_lido=="":
        QMessageBox.about(janela,"Nome:", "Nenhum nome foi digitado")
    else:
        #Idade
        dado_lido2 = janela.LeIdade.text()

        #Confere Idade se n estiver vazio
        if dado_lido2=="":
            QMessageBox.about(janela,"Idade:", "Idade Vazia")
        else:
            #Sexo
            if janela.Rb1.isChecked():
                dado_lido3= 'M'
            elif janela.Rb2.isChecked():
                dado_lido3= 'F'
            else:
                dado_lido3= 'ND'

            #Escolaridade
            dado_lido4=janela.CbEscol.currentText()

            #Juntar tudo
            dados = "Nome: "+dado_lido+"\nIdade: "+dado_lido2+"\nSexo: "+dado_lido3+"\nEscolaridade: "+dado_lido4

            #Esvaziar
            janela.LeNome.setText("")
            janela.LeIdade.setText("")

            #Adicionar a Lista msm
            janela.Lista.addItem(dados)

            #Contador
            contar_itens()

def deletar():
    result = QMessageBox.question(janela, "Excluir Itens", "Deseja mesmo excluir todos os itens da Lista?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.Lista.clear()
        contar_itens()

def contar_itens():
    valor = janela.Lista.count() 
    janela.LbConta.setText("Nº de Itens: " + str(valor))

def ordenar():
    janela.Lista.sortItems()


#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("caixa_mensagens.ui")

janela.BtFechar.clicked.connect(fechar_tela)
janela.BtAdicionar.clicked.connect(listar_dados)
janela.BtExcluir.clicked.connect(deletar)
janela.BtOrdenar.clicked.connect(ordenar)

janela.show()
app.exec()