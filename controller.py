class Controller:
    def __init__(self, view_1, view_2, model) -> None:
        self.view_1 = view_1
        self.view_2 = view_2
        self.model = model

    
    def ctr_logar(self, dicionario):

        self.model.mdl_logar(dicionario)

    def ctr_mwindow(self):
        self.view_1.hide()
        self.view_2.show()
        self.ctr_dados_tabela()

    def ctr_dados_tabela(self):
        self.dados=self.model.dados_tabela()

    def ctr_preenche(self, dice, i):
        self.view_2.preencher(dice, i)

    def psq_projeto(self, item1):
        self.item = item1
        self.model.src_projeto(self.item)

    def psq_aluno(self, item1):
        self.item = item1
        self.model.src_aluno(self.item)

    def ctr_inserir(self, lista):
        self.lista = lista
        self.model.mdl_inserir(self.lista)

    def ctr_atualizar(self, item, lista):
        self.item = item
        self.lista = lista
        self.model.mdl_atualizar(self.item, self.lista)

    def ctr_excluir (self, item):
        self.item = item
        self.model.mdl_excluir(self.item)
