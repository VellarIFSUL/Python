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

def CallCadProduto():
    telaCadastroProduto.show()
    telaListaProdutos.close()

def CadProduto():
    janela = telaCadastroProduto
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

def PDFProdutos():
    janela = telaListaProdutos
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

def CallEditarProduto():
    janela=telaListaProdutos
    global numero_id 
    try:
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
    except:
        QMessageBox.critical(janela,"Erro", "Nenhuma Linha selecionada!")

def ExcluirProduto():
    janela = telaListaProdutos
    try:
        linha = janela.tableWidget.currentRow()
        janela.tableWidget.removeRow(linha)
        Cursor.execute("SELECT id FROM produtos")
        dados_lidos = Cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        Cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))
        BD.commit()
    except:
        QMessageBox.critical(janela,"Erro", "Nenhuma Linha Selecionada")

def EnviarEditProdutos():
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
    telaListaProdutos.close()
    CallProdutos()

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

def CallCadUsuario():
    telaCadastro.show()

def CadUsuario():
    janela = telaCadastro
    nome = janela.lineEditUser.text()
    senha = janela.lineEditPassword.text()
    senha2 = janela.lineEditPasswordAgain.text()

    if(nome==""):
        QMessageBox.critical(janela,"Erro", "Nome vazio!")
    elif((senha=="")and(senha2=="")):
        QMessageBox.critical(janela,"Erro", "Senhas Vazio!")
    elif(senha!=senha2):
        QMessageBox.critical(janela,"Erro", "Senhas diferente!")
    else:
        try:
            comando_SQL = "INSERT INTO usuario (nome, senha) VALUES (%s,%s)"
            dados = (nome, senha)
            Cursor.execute(comando_SQL,dados)
            BD.commit()
        except:
            QMessageBox.critical(janela,"Aviso","Usuário já cadastrado")
        else:
            QMessageBox.about(janela,"Aviso","Usuário cadastrado com sucesso")
            janela.close()

def CallProdutos():
    telaListaProdutos.show()
    janela = telaListaProdutos
    Cursor.execute("SELECT * FROM produtos")
    dados_lidos = Cursor.fetchall()
    janela.tableWidget.setRowCount(len(dados_lidos))
    janela.tableWidget.setColumnCount(4)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            janela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    pass

def CallClientes():
    telaListaClientes.show()
    janela = telaListaClientes
    Cursor.execute("SELECT * FROM cliente")
    dados_lidos = Cursor.fetchall()
    janela.tableWidget.setRowCount(len(dados_lidos))
    janela.tableWidget.setColumnCount(4)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            janela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    pass

def PDFClientes():
    janela = telaListaClientes
    Cursor.execute("SELECT * FROM cliente")
    dados_lidos = Cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_clientes.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800,"Clientes:")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10,750,"CPF")
    pdf.drawString(110,750,"EMAIL")
    pdf.drawString(250,750,"NOME")
    pdf.drawString(350,750,"TELEFONE")
    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(250,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(350,750 - y, str(dados_lidos[i][3]))
    pdf.save()
    QMessageBox.information(janela,"PDF", "PDF GERADO")
    pass

def ExcluirCliente():
    janela = telaListaClientes
    try:
        linha = janela.tableWidget.currentRow()
        janela.tableWidget.removeRow(linha)
        Cursor.execute("SELECT CPF FROM cliente")
        dados_lidos = Cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        Cursor.execute("DELETE FROM cliente WHERE CPF="+ str(valor_id))
        BD.commit()
    except:
        QMessageBox.critical(janela,"Erro", "Nenhuma Linha Selecionada")
    pass

def CallCadCliente():
    telaCadastroCliente.show()
    telaListaClientes.close()

def CadCliente():
    janela = telaCadastroCliente
    CPF=janela.lineEditCPF.text()
    nome=janela.lineEditNome.text()
    email=janela.lineEditEmail.text().casefold()
    telefone=janela.lineEditTelefone.text()
    if(not(CPF.isnumeric() and (len(CPF)==11))):
        QMessageBox.critical(janela,"Erro", "CPF Invalido!")
        janela.lineEditCPF.setText("")
    elif(nome==""):
        QMessageBox.critical(janela,"Erro", "Nome vazio!")
    elif((email.find("@")<1)or(email.find(".")<1)):
        QMessageBox.critical(janela,"Erro", "Email invalido!")
        janela.lineEditEmail.setText("")
    elif(not telefone.isnumeric()):
        QMessageBox.critical(janela,"Erro", "Telefone Invalido")
        janela.lineEditTelefone.setText("")
    else:
        try:
            comando_SQL = "INSERT INTO cliente (CPF, email, nome, telefone) VALUES (%s,%s,%s,%s)"
            dados = (CPF,email,nome,telefone)
            Cursor.execute(comando_SQL,dados)
            BD.commit()
        except:
            QMessageBox.critical(janela,"Aviso","Cliente já cadastrado")
            janela.lineEditCPF.setText("")
        else:
            QMessageBox.about(janela,"Aviso","Cliente cadastrado com sucesso")
            janela.lineEditCPF.setText("")
            janela.lineEditNome.setText("")
            janela.lineEditEmail.setText("")
            janela.lineEditTelefone.setText("")
    pass

def CallEditarCliente():
    QMessageBox.information(telaListaClientes,"Ops", "Ops, essa função ainda n esta disponivel :(")
    pass

def CallVendas():
    QMessageBox.information(telaPrincipal,"Ops", "Ops, essa função ainda n esta disponivel :(")
    pass
def CallUsuarios():
    QMessageBox.information(telaPrincipal,"Ops", "Ops, essa função ainda n esta disponivel :(")
    pass


#programa principal
app=QtWidgets.QApplication([])

telaLogin=uic.loadUi("telaLogin.ui")
telaLogin.btnLogar.clicked.connect(Logar)
telaLogin.btnCad.clicked.connect(CallCadUsuario)

telaCadastro=uic.loadUi("telaCadUsuario.ui")
telaCadastro.btnCad.clicked.connect(CadUsuario)

telaPrincipal=uic.loadUi("telaPrincipal.ui")
telaPrincipal.btnProdutos.clicked.connect(CallProdutos)
telaPrincipal.btnClientes.clicked.connect(CallClientes)
telaPrincipal.btnVendas.clicked.connect(CallVendas)
telaPrincipal.btnUsuarios.clicked.connect(CallUsuarios)

telaListaProdutos=uic.loadUi("telaListaProdutos.ui")
telaListaProdutos.btnPDF.clicked.connect(PDFProdutos)
telaListaProdutos.btnEditar.clicked.connect(CallEditarProduto)
telaListaProdutos.btnExcluir.clicked.connect(ExcluirProduto)
telaListaProdutos.btnCad.clicked.connect(CallCadProduto)

telaCadastroProduto=uic.loadUi("telaCadProduto.ui")
telaCadastroProduto.btnEnviar.clicked.connect(CadProduto)


telaEditar=uic.loadUi("telaEditProduto.ui")
telaEditar.btnSalvar.clicked.connect(EnviarEditProdutos)

telaListaClientes=uic.loadUi("telaListaClientes.ui")
telaListaClientes.btnPDF.clicked.connect(PDFClientes)
telaListaClientes.btnEditar.clicked.connect(CallEditarCliente)
telaListaClientes.btnExcluir.clicked.connect(ExcluirCliente)
telaListaClientes.btnCad.clicked.connect(CallCadCliente)

telaCadastroCliente=uic.loadUi("telaCadCliente.ui")
telaCadastroCliente.btnEnviar.clicked.connect(CadCliente)

telaLogin.show()
app.exec()