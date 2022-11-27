#importar bibliotecas:
from PyQt5 import uic,QtWidgets
from pyUFbr.baseuf import ufbr
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
        telaEditProduto.show()
        janela=telaEditProduto
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
    janela=telaEditProduto
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
    janela.tableWidget.setColumnCount(6)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
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
        if QMessageBox.question(janela, "Excluir", "Deseja mesmo excluir?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
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
    telaCadastroCliente.cBEstado.setEditable(True)
    telaCadastroCliente.cBEstado.addItems(ufbr.list_uf)
    telaListaClientes.close()

def filtrocidadesCadCliente():
    telaCadastroCliente.cBCidade.clear()
    cidades= (ufbr.list_cidades(telaCadastroCliente.cBEstado.currentText()))
    telaCadastroCliente.cBCidade.addItems(cidades)

def CadCliente():
    janela = telaCadastroCliente
    CPF=janela.lineEditCPF.text()
    nome=janela.lineEditNome.text()
    email=janela.lineEditEmail.text().casefold()
    telefone=janela.lineEditTelefone.text()
    estado=janela.cBEstado.currentText()
    cidade=janela.cBCidade.currentText()
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
            comando_SQL = "INSERT INTO cliente (CPF, email, nome, telefone, Estado, Cidade) VALUES (%s,%s,%s,%s,%s,%s)"
            dados = (CPF,email,nome,telefone,estado,cidade)
            Cursor.execute(comando_SQL,dados)
            BD.commit()
        except:
            QMessageBox.critical(janela,"Aviso","Erro no cadastro")
            janela.lineEditCPF.setText("")
        else:
            QMessageBox.about(janela,"Aviso","Cliente cadastrado com sucesso")
            janela.lineEditCPF.setText("")
            janela.lineEditNome.setText("")
            janela.lineEditEmail.setText("")
            janela.lineEditTelefone.setText("")
    pass

def CallEditarCliente():
    janela=telaListaClientes
    global numero_cpf
    try:
        linha = janela.tableWidget.currentRow()
        Cursor.execute("SELECT CPF FROM cliente")
        dados_lidos = Cursor.fetchall() #pega todos os resultados do select e armazena em uma tupla
        valor_cpf = dados_lidos[linha][0]
        Cursor.execute("SELECT * FROM cliente WHERE CPF="+ str(valor_cpf))
        cliente = Cursor.fetchall()
        telaEditCliente.show()
        janela=telaEditCliente
        janela.lineEditCPF.setText(str(cliente[0][0]))
        janela.lineEditEmail.setText(str(cliente[0][1]))
        janela.lineEditNome.setText(str(cliente[0][2]))
        janela.lineEditTelefone.setText(str(cliente[0][3]))
        

        janela.cBEstado.setEditable(True)
        janela.cBEstado.addItems(ufbr.list_uf)

        index = janela.cBEstado.findData(str(cliente[0][4]))
        if(index != -1):
            janela.cBEstado.setCurrentIndex(index)

        index = janela.cBCidade.findData(str(cliente[0][5]))
        if(index != -1):
            janela.cBCidade.setCurrentIndex(index)
        
        numero_cpf = valor_cpf
    except:
        QMessageBox.critical(janela,"Erro", "Nenhuma Linha selecionada!")
    pass

def filtrocidadesEditCliente():
    telaEditCliente.cBCidade.clear()
    cidades= (ufbr.list_cidades(telaEditCliente.cBEstado.currentText()))
    telaEditCliente.cBCidade.addItems(cidades)

def EnviarEditClientes():
    try:
        global numero_cpf
        # ler dados do lineEdit
        janela=telaEditCliente
        CPF = janela.lineEditCPF.text()
        nome = janela.lineEditNome.text()
        email = janela.lineEditEmail.text()
        telefone = janela.lineEditTelefone.text()
        estado=janela.cBEstado.currentText()
        cidade=janela.cBCidade.currentText()
        # atualizar os dados no banco
        Cursor.execute("UPDATE cliente SET CPF = '{}', email ='{}', nome ='{}', telefone ='{}', Estado ='{}', Cidade ='{}' WHERE CPF ={}".format(CPF,email,nome,telefone,estado,cidade,numero_cpf))
        BD.commit()
        #atualizar as janelas
        janela.close()
        telaListaClientes.close()
        CallClientes()
    except:
        QMessageBox.critical(janela,"Erro", "Ops, algo aconteceu")
    pass

def CallVendas():
    telaListaVendas.show()
    janela = telaListaVendas
    Cursor.execute("SELECT v.ID, p.descricao, c.nome, v.Quantidade, p.preco, (p.preco*v.Quantidade) FROM vendas v INNER JOIN produtos p ON v.Produto=p.id INNER JOIN Cliente c ON v.Cliente=c.CPF;")
    dados_lidos = Cursor.fetchall()
    janela.tableWidget.setRowCount(len(dados_lidos))
    janela.tableWidget.setColumnCount(6)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            janela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    pass

def CallUsuarios():
    telaListaUsuarios.show()
    janela = telaListaUsuarios
    Cursor.execute("SELECT * FROM usuario")
    dados_lidos = Cursor.fetchall()
    janela.tableWidget.setRowCount(len(dados_lidos))
    janela.tableWidget.setColumnCount(1)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 1):
            janela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    pass

def CallEditarUsuario():
    janela=telaListaUsuarios
    global nome_usuario
    try:
        linha = janela.tableWidget.currentRow()
        Cursor.execute("SELECT nome FROM usuario")
        dados_lidos = Cursor.fetchall() #pega todos os resultados do select e armazena em uma tupla
        Cursor.execute("SELECT * FROM usuario WHERE nome = '"+ str(dados_lidos[linha][0])+"';")
        usuario = Cursor.fetchall()
        telaEditUsuario.show()
        janela=telaEditUsuario
        janela.lineEditUsuario.setText(str(usuario[0][0]))
        nome_usuario = usuario[0][0]
    except:
        QMessageBox.critical(janela,"Erro", "Nenhuma Linha selecionada!")
    pass

def EnviarEditUsuario():
    global nome_usuario
    # ler dados do lineEdit
    janela=telaEditUsuario
    usuario = janela.lineEditUsuario.text()
    senha = janela.lineEditSenha.text()
    if senha == "":
    # atualizar os dados no banco
        Cursor.execute("UPDATE usuario SET nome = '{}' WHERE nome ='{}'".format(usuario,nome_usuario))
    else:
        Cursor.execute("UPDATE usuario SET nome = '{}', senha ='{}' WHERE nome ='{}'".format(usuario,senha,nome_usuario))
    BD.commit()
    #atualizar as janelas
    janela.close()
    telaListaUsuarios.close()
    CallUsuarios()
    pass

def ExcluirUsuario():
    janela = telaListaUsuarios
    try:
        if QMessageBox.question(janela, "Excluir", "Deseja mesmo excluir?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
            linha = janela.tableWidget.currentRow()
            janela.tableWidget.removeRow(linha)
            Cursor.execute("SELECT nome FROM usuario")
            dados_lidos = Cursor.fetchall()
            valor_id = dados_lidos[linha][0]
            Cursor.execute("DELETE FROM usuario WHERE nome='"+ str(valor_id)+"';")
            BD.commit()
    except:
        QMessageBox.critical(janela,"Erro", "Nenhuma Linha Selecionada")
    pass

def PDFUsuarios():
    janela = telaListaUsuarios
    Cursor.execute("SELECT nome FROM usuario")
    dados_lidos = Cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Usuarios.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800,"Usuarios:")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10,750,"Nome")
    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
    pdf.save()
    QMessageBox.information(janela,"PDF", "PDF GERADO")

def ExcluirVenda():
    janela = telaListaVendas
    try:
        if QMessageBox.question(janela, "Excluir", "Deseja mesmo excluir?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
            linha = janela.tableWidget.currentRow()
            janela.tableWidget.removeRow(linha)
            Cursor.execute("SELECT ID FROM vendas")
            dados_lidos = Cursor.fetchall()
            valor_id = dados_lidos[linha][0]
            Cursor.execute("DELETE FROM vendas WHERE ID="+ str(valor_id))
            BD.commit()
    except:
        QMessageBox.critical(janela,"Erro", "Nenhuma Linha Selecionada")
    pass
    pass

def PDFVendas():
    janela = telaListaVendas
    Cursor.execute("SELECT v.ID, p.descricao, c.nome, v.Quantidade, p.preco, (p.preco*v.Quantidade) FROM vendas v INNER JOIN produtos p ON v.Produto=p.id INNER JOIN Cliente c ON v.Cliente=c.CPF;")
    dados_lidos = Cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Vendas.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800,"Usuarios:")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10,750,"ID")
    pdf.drawString(110,750,"PRODUTO")
    pdf.drawString(250,750,"CLIENTE")
    pdf.drawString(350,750,"QUANTIDADE")
    pdf.drawString(450,750,"PREÇO")
    pdf.drawString(550,750,"TOTAL")
    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(250,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(350,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(450,750 - y, str(dados_lidos[i][4]))
        pdf.drawString(550,750 - y, str(dados_lidos[i][5]))
    pdf.save()
    pass

def CallCadVenda():
    telaCadastroVendas.show()
    janela=telaCadastroVendas
    janela.cBProduto.clear()
    janela.cBCliente.clear()
    Cursor.execute("SELECT descricao, preco, id FROM produtos")
    produtos = Cursor.fetchall()
    global Produtos 
    Produtos = produtos
    for prod in produtos:
        janela.cBProduto.addItem(str(prod[0]))
    Cursor.execute("SELECT nome, CPF FROM cliente")
    clientes = Cursor.fetchall()
    global Clientes
    Clientes = clientes
    for cli in clientes:
        janela.cBCliente.addItem(str(cli[0]))
    pass

def CalculaPreco():
    janela = telaCadastroVendas
    try:
        i = janela.cBProduto.currentIndex()
        qnt = janela.sBQuantidade.value()
        valorTotal = Produtos[i][1]*qnt
        janela.lblTotal.clear()
        janela.lblTotal.setText('Total: '+str(valorTotal))
    except:
        janela.lblTotal.setText('Ero nu sistema!')
    pass

#TESTAR
def CadVenda():
    janela = telaCadastroVendas
    try:
        p = janela.cBProduto.currentIndex()
        p = Produtos[p][2]
    except:
        p = ''
    try:
        c = janela.cBCliente.currentIndex()
        c = Clientes[c][1]
    except:
        c = ''
    q = janela.sBQuantidade.value()

    if(p!="" and c!=""):
        try:
            Cursor.execute("INSERT INTO vendas (Produto,Cliente,Quantidade) VALUES (%s,%s,%s)",(str(p),str(c),str(q)))
            BD.commit()
        except:
            QMessageBox.critical(janela,"Erro", "Ops! Algo deu Errado")
        else:
            telaListaVendas.close()
            janela.close()
            CallVendas()
        pass
    else:
        QMessageBox.critical(janela,"Erro", "Ops! Algo deu Errado")
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

telaEditProduto=uic.loadUi("telaEditProduto.ui")
telaEditProduto.btnSalvar.clicked.connect(EnviarEditProdutos)

telaEditCliente=uic.loadUi("telaEditCliente.ui")
telaEditCliente.cBEstado.currentIndexChanged.connect(filtrocidadesEditCliente)
telaEditCliente.btnSalvar.clicked.connect(EnviarEditClientes)

telaListaClientes=uic.loadUi("telaListaClientes.ui")
telaListaClientes.btnPDF.clicked.connect(PDFClientes)
telaListaClientes.btnEditar.clicked.connect(CallEditarCliente)
telaListaClientes.btnExcluir.clicked.connect(ExcluirCliente)
telaListaClientes.btnCad.clicked.connect(CallCadCliente)

telaCadastroCliente=uic.loadUi("telaCadCliente.ui")
telaCadastroCliente.cBEstado.currentIndexChanged.connect(filtrocidadesCadCliente)
telaCadastroCliente.btnEnviar.clicked.connect(CadCliente)

telaListaUsuarios=uic.loadUi("telaListaUsuarios.ui")
telaListaUsuarios.btnEditar.clicked.connect(CallEditarUsuario)
telaListaUsuarios.btnExcluir.clicked.connect(ExcluirUsuario)
telaListaUsuarios.btnPDF.clicked.connect(PDFUsuarios)

telaEditUsuario=uic.loadUi("telaEditUsuario.ui")
telaEditUsuario.btnSalvar.clicked.connect(EnviarEditUsuario)

telaListaVendas=uic.loadUi("telaListaVendas.ui")
telaListaVendas.btnExcluir.clicked.connect(ExcluirVenda)
telaListaVendas.btnPDF.clicked.connect(PDFVendas)
telaListaVendas.btnCad.clicked.connect(CallCadVenda)

telaCadastroVendas=uic.loadUi("TelaCadVenda.ui")
telaCadastroVendas.btnEnviar.clicked.connect(CadVenda)
telaCadastroVendas.cBProduto.currentIndexChanged.connect(CalculaPreco)
telaCadastroVendas.sBQuantidade.valueChanged.connect(CalculaPreco)

telaLogin.show()
app.exec()