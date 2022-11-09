#importar bibliotecas:
from PyQt5 import uic,QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from reportlab.pdfgen import canvas

BD = mysql.connector.connect (
 host="localhost",
 user="root",
 passwd="",
 database="sistemapy"
)
Cursor = BD.cursor()


def Enviar():
    janela = telaPrincipal
    desc = janela.lineEditDesc.text()
    preco = janela.spinBoxPreco.value()

    if janela.rbInfo.isChecked():
        categoria="Informatica"
    elif janela.rbAli.isChecked():
        categoria="Alimentos"
    else:
        categoria="Eletronicos"
    
    janela.lineEditDesc.setText("")
    janela.spinBoxPreco.setValue(0.00)
    janela.rbInfo.setChecked(True)

    sqlEntry = "INSERT INTO produtos(descricao,preco,categoria) VALUES (%s,%s,%s)"
    dados = (desc,str(preco),categoria)
    Cursor.execute(sqlEntry,dados)
    BD.commit()

def Listar():
    telaListar.show()
    janela = telaListar
    Cursor.execute("SELECT * FROM produtos")
    dados_lidos = Cursor.fetchall()
    janela.tableWidget.setRowCount(len(dados_lidos))
    janela.tableWidget.setColumnCount(4)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            janela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def PDFizar():
    janela = telaListar
    Cursor.execute("SELECT * FROM produtos")
    dados_lidos = Cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800,"Produtos Cadastrados:")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10,750,"ID")
    pdf.drawString(110,750,"PRODUTO")
    pdf.drawString(250,750,"PREÇO")
    pdf.drawString(350,750,"CATEGORIA")
    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(250,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(350,750 - y, str(dados_lidos[i][3]))
    pdf.save()
    QMessageBox.information(janela,"PDF", "PDF GERADO")

def Editar():
    janela=telaListar
    global numero_id #variável global que serve para mostrar o id que está sendo mostrado na tela
    linha = janela.tableWidget.currentRow()
    Cursor.execute("SELECT id FROM produtos")
    dados_lidos = Cursor.fetchall() #pega todos os resultados do select e armazena em uma tupla
    valor_id = dados_lidos[linha][0]
    Cursor.execute("SELECT * FROM produtos WHERE id="+ str(valor_id))
    produto = Cursor.fetchall()
    telaEditar.show()
    janela=telaEditar
    janela.lineEditDesc.setText(str(produto[0][1]))
    janela.spinBoxPreco.setValue(produto[0][2])
    janela.lineEditCat.setText(str(produto[0][3]))
    numero_id = valor_id

def Excluir():
    janela = telaListar
    linha = janela.tableWidget.currentRow()
    janela.tableWidget.removeRow(linha)
    Cursor.execute("SELECT id FROM produtos")
    dados_lidos = Cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    Cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))
    BD.commit()

def EnviarEdit():
    global numero_id
    # ler dados do lineEdit
    janela=telaEditar
    descricao = janela.lineEditDesc.text()
    preco = janela.spinBoxPreco.value()
    categoria = janela.lineEditCat.text()
    # atualizar os dados no banco
    Cursor.execute("UPDATE produtos SET descricao = '{}', preco ='{}', categoria ='{}' WHERE id ={}".format(descricao,preco,categoria,numero_id))
    BD.commit()
    #atualizar as janelas
    janela.close()
    telaListar.close()
    Listar()

def Logar():
    janela=telaLogin
    nome = janela.lineEditUser.text()
    senha = janela.lineEditPassword.text()
    janela.lineEditUser.setText("")
    janela.lineEditPassword.setText("")
    if((nome!="")and(senha!="")):
        Cursor.execute("SELECT nome, senha FROM usuario WHERE nome='{}'".format(nome))
        senha_bd = Cursor.fetchall()
        try:
            nomeBD=senha_bd[0][0]
            senhaBD=senha_bd[0][1]
        except:
            nomeBD=""
            senhaBD=""
        finally:
            if (nomeBD==nome) and (senhaBD==senha):
                janela.close()
                telaPrincipal.show()
            else:
                QMessageBox.critical(janela,"Erro", "Informações não batem!")
    else:
        QMessageBox.critical(janela,"Erro", "Nenhum dado preenchido!")

def Cadastrar():
    pass

#programa principal
app=QtWidgets.QApplication([])

telaLogin=uic.loadUi("telaLogin.ui")
telaLogin.btnLogar.clicked.connect(Logar)
telaLogin.btnCad.clicked.connect(Cadastrar)

telaPrincipal=uic.loadUi("telaPrincipal.ui")
telaPrincipal.btnEnviar.clicked.connect(Enviar)
telaPrincipal.btnListar.clicked.connect(Listar)

telaListar=uic.loadUi("telaListar.ui")
telaListar.btnPDF.clicked.connect(PDFizar)
telaListar.btnEditar.clicked.connect(Editar)
telaListar.btnExcluir.clicked.connect(Excluir)

telaEditar=uic.loadUi("telaEditar.ui")
telaEditar.btnSalvar.clicked.connect(EnviarEdit)

telaLogin.show()
app.exec()