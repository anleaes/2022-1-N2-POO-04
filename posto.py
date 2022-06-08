from endereco import *

class Posto:
    def __init__(self, endereco, nome_posto, telefone,cnpj):
        #super(Posto,self) .__init__(cep,rua,bairro,cidade)
        self.endereco = endereco
        self.nome_posto = nome_posto
        self.telefone = telefone
        self.cnpj = cnpj
    
    def endereco_posto_paciente(self):
        return print("o posto fica na rua: ",self.endereco.rua)
    def nome_do_posto(self):
        return print(self.nome_posto)
        


posto01 = Posto(end01, 'posto saude', '3245-11-936', '6565665' )
posto02 = Posto(end02, 'posto modelo', '2222-11-936', '9999999' )




        
        