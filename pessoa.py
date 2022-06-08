from endereco import Endereco

class Pessoa(Endereco):
    def __init__(self, nome,cpf, rg, idade, cep,rua,bairro,cidade, ):
        super(Pessoa,self) .__init__(cep,rua,bairro,cidade)
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
    
    def endereco_casa_pessoa(self):
        return print("endereço da rua da", self.nome, "é: ", self.rua)
    

p1 = Pessoa('veronica', '400.289.22', 558893, 18,'91780-999', 'ipiranga 241', 'vila nova', 'poa')
p2 = Pessoa('greice', '5573676', 558893, 33,'88888-999', 'cap. amarantes xavier 241', 'campo novo', 'canoas')

#mano aqui quando chamo o metodo, pede para nós declarar todos os atributos
#inclusive os atributos que estão dentro da super classe (cep,rua,bairro,cidade)
