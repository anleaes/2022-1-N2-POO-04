from endereco import *

class Posto(Endereco):
    def __init__(self, cep, rua,bairro,cidade, nome_posto, telefone,cnpj):
        super(Posto,self) .__init__(cep,rua,bairro,cidade)
        self.nome_posto = nome_posto
        self.telefone = telefone
        self.cnpj = cnpj
    
    def endereco_posto_paciente(self):
        return print("o posto fica na rua %i ",self.endereco.rua)
    def nome_do_posto(self):
        return print(self.nome_posto)
        


posto01 = Posto('91790-850', 'voluntarios', 'centro', 'poa', 'posto saude', '3245-11-936', '6565665' )
posto02 = Posto('91766-66', 'andradas', 'joaquina', 'CANOAS', 'posto modelo', '2222-11-936', '9999999' )


        
        