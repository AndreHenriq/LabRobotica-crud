import datetime
import res
import sys
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import *

class logar(QWidget):
    def __init__(self):
        super(logar,self).__init__()
        self.resize(499, 256)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        uic.loadUi("Login.ui",self)

        #atribui o botao a uma variavel
        self.button = self.findChild(QPushButton, 'pushButton')
        self.usr= self.findChild(QLineEdit, 'lineEdit')
        self.pwd= self.findChild(QLineEdit, 'lineEdit_2')

        #faz algo com o botao
        self.button.clicked.connect(self.btn_logar)
        
        #mostra tela
        #self.show()
    #funções de movimentar a tela
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.dragPos )
        self.dragPos = event.globalPos()
        event.accept()

    #recebe referencia do controller
    def set_controller(self,controller):
        self.controller=controller

    def btn_logar(self):
        #Responsabilidade do model
        self.controller.ctr_logar({self.usr.text(): self.pwd.text()})


class MWindow(QMainWindow):
    def __init__(self):
        super(MWindow, self).__init__()
        uic.loadUi("projeto.ui", self)
        self.table = self.findChild(QtWidgets.QTableWidget,"tableWidget")        
        
        #"ancora" para redimensionar a tela
        self.size_grp = self.findChild(QtWidgets.QPushButton,"size_grip")
        QSizeGrip(self.size_grp)
        
        self.resize(512,628)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        #findchild para encontrar o objeto no arquivo.ui
        self.btnFechar = self.findChild(QPushButton, 'fechar')
        self.btnFechar.clicked.connect(self.close)
        
        self.btn_pesquisa_aluno = self.findChild(QPushButton, 'pesquisar_aluno')
        self.btn_pesquisa_aluno.clicked.connect(self.pesca_aluno)

        self.ln_proj = self.findChild(QLineEdit, 'ln_projeto')
        self.btn_pesquisa_projeto = self.findChild(QPushButton, 'pesquisar_projeto')
        self.btn_pesquisa_projeto.clicked.connect(self.pesca_projeto)


        self.btn_insere = self.findChild(QPushButton, 'btn_inserir')
        self.btn_insere.clicked.connect(self.inserir)

        self.btn_atualiza = self.findChild(QPushButton, 'btn_atualizar')
        self.btn_atualiza.clicked.connect(self.atualizar)

        self.btn_exclui = self.findChild(QPushButton, 'btn_excluir')
        self.btn_exclui.clicked.connect(self.excluir)

        self.ln_material = self.findChild(QLineEdit, 'ln_materiais')
        self.ln_data = self.findChild(QDateEdit, 'dateEdit')

        self.index=self.table.selectionModel().selectionChanged.connect(self.seleciona_row)
    
    def set_controller(self, controller):
        self.controller=controller

    def consulta_banco(self):        
        self.controller.ctr_dados_tabela()

    def inserir(self):
        self.materiais = self.ln_material.text().split(",")
        self.lista = {"Aluno": self.ln_aluno.text(),
                        "Projeto": self.ln_projeto.text(),
                        "Data": self.ln_data.dateTime().toPyDateTime(),
                        "Materiais":self.materiais}
        
        self.controller.ctr_inserir(self.lista)

    def atualizar(self):
        self.materiais = self.ln_material.text().split(',')
        self.item = {"Aluno": self.ln_aluno.text()}
        self.lista = {"Aluno": self.ln_aluno.text(),
                        "Projeto": self.ln_projeto.text(),
                        "Data": self.ln_data.dateTime().toPyDateTime(),
                        "Materiais":self.materiais}

        self.controller.ctr_atualizar(self.item, self.lista)

    def excluir(self):
        self.item = self.ln_projeto.text()
        self.controller.ctr_excluir(self.item)

    def pesca_aluno(self):
        self.aluno = self.ln_aluno.text()
        self.controller.psq_aluno(self.aluno)

    def pesca_projeto(self):
        self.projeto = self.ln_projeto.text()
        self.controller.psq_projeto(self.projeto)

    def pesca_data(self):
        self.data = self.ln_aluno.text()
        self.controller.psq_aluno(self.aluno)

    def preencher(self, info, i):
        self.info = info
        self.table.setRowCount(i+1)
        self.combo = QComboBox()
        self.combo.addItems(self.info['Materiais'])
        self.table.setCellWidget(i,3, self.combo)
        self.table.setItem(i, 0, QTableWidgetItem(self.info['Aluno']))
        self.table.setItem(i, 1, QTableWidgetItem(self.info['Projeto']))
        self.table.setItem(i, 2, QTableWidgetItem(str(self.info['Data'])))

    def seleciona_row(self, selected):
        for i in selected.indexes():
            self.tbl_text=self.table.item(i.row(), i.column())       

            #envia o item da tabela para os campos
            self.ln_aluno = self.findChild(QLineEdit, 'ln_aluno')
            self.ln_projeto = self.findChild(QLineEdit, 'ln_projeto')
            self.ln_data = self.findChild(QDateEdit, 'dateEdit')
            self.ln_aluno.setText(self.table.item(i.row(), 0).text())
            self.ln_projeto.setText(self.table.item(i.row(), 1).text())
            
            self.dia_str = self.table.item(i.row(), 2).text()
            self.date = self.dia_str.split(None, 2)
            self.dia_str= self.date[0].split("-")
            self.dia=""
            for i in self.dia_str:
                self.dia += i
            #print(self.dia)
            self.qdate = QtCore.QDate.fromString(self.dia, "yyyyMMdd")
            #print(self.qdate)
            self.ln_data.setDate(self.qdate)

    def close(self):
        app = QApplication(sys.argv)
        sys.exit(app.exec_())
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPos() - self.dragPos )
        self.dragPos = event.globalPos()
        event.accept()


