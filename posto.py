from endereco import *

class Posto(Endereco):
    def __init__(self, cep, rua,bairro,cidade, nome):
        super(Posto,self) .__init__(cep,rua,bairro,cidade)
        self.nome = nome
        
        