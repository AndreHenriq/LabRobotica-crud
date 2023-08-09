from pymongo import MongoClient

class Model:

    def conecta(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.loginDB
        self.collection = self.db.signin
        self.collection_2 = self.db.registros
        return self.db

    def set_controller(self,controller):
        self.controller=controller

    def mdl_logar(self, dicionario):
        dao=self.conecta()
        self.sign_in= dao.signin
        if self.sign_in.find_one(dicionario):
            self.controller.ctr_mwindow()
        else: 
            print('usuario nao encontrado')

    def dados_tabela(self):
        dao=self.conecta()
        self.registros=dao.registros
        self.dados=[]
        for registros in self.registros.find():
            self.dados.append(registros)

        for i in range(len(self.dados)):
            self.controller.ctr_preenche(self.dados[i], i)

    def src_projeto (self, item2):
        self.item = item2
        if item2 == "":
            self.controller.ctr_dados_tabela()
        else:

            dao=self.conecta()
            self.registros=dao.registros
            self.dados=[]
            for registros in self.registros.find({"Projeto":self.item}):
                self.dados.append(registros)

            #print(self.dados)
            for i in range(len(self.dados)):
                self.controller.ctr_preenche(self.dados[i], i)

    def src_aluno (self, item2):
            self.item = item2
            if item2 == "":
                self.controller.ctr_dados_tabela()
            else:
                dao=self.conecta()
                self.registros=dao.registros
                self.dados=[]
                for registros in self.registros.find({"Aluno":self.item}):
                    self.dados.append(registros)

            for i in range(len(self.dados)):
                self.controller.ctr_preenche(self.dados[i], i)

    def mdl_inserir (self, lista):

        self.lista = lista
        print(self.lista)
        dao=self.conecta()
        dao.registros.insert_one(self.lista)

    def mdl_atualizar(self, item, lista):
        self.item = item
        self.lista = lista
        #print (self.item)

        dao = self.conecta()
        self.registros = dao.registros
        self.registros.update_one(self.item, {"$set": self.lista}, upsert=False)

    def mdl_excluir (self, item):
        self.item = item
        dao = self.conecta()
        self.registro = dao.registros
        #print(self.item)
        self.registros.delete_one({"Projeto": self.item})
        
        print('Item excluido!')
