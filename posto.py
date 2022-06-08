from endereco import *

class Posto(Endereco):
    def __init__(self, cep, rua,bairro,cidade, nome, telefone,cnpj):
        super(Posto,self) .__init__(cep,rua,bairro,cidade)
        self.nome = nome
        self.telefone = telefone
        self.cnpj = cnpj
        


posto01 = Posto('91780-999', 'ipiranga 255', 'jardim','poa', 'posto saude', '3245-11-936', '6565665' )
posto02 = Posto('6666-999', 'pau brasil 255', 'hipica','canoas', 'posto modelo', '2222-11-936', '9999999' )


        
        