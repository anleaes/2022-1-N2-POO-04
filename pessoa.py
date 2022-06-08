from endereco import Endereco

class Pessoa(Endereco):
    def __init__(self, cep,rua,bairro,cidade, nome,cpf, rg, idade):
        super(Pessoa,self) .__init__(cep,rua,bairro,cidade)
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
    
    def endereco_casa_pessoa(self):
        return print("endereço da rua da %i ", self.nome, "é %i", self.rua)
    

p1 = Pessoa('veronica', '400.289.22', 558893, 18)
p2 = Pessoa('greice', '5573676', 558893, 33)