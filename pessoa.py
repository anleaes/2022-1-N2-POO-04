from endereco import *

class Pessoa(Endereco):
    def __init__(self, cep, rua,bairro,cidade, nome,cpf, rg, idade):
        super(Pessoa,self) .__init__(cep,rua,bairro,cidade)
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        
        