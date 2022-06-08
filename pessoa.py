from endereco import Endereco

class Pessoa(Endereco):
    def __init__(self, cep, rua,bairro,cidade, nome,cpf, rg, idade):
        super(Pessoa,self) .__init__(cep,rua,bairro,cidade)
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
        
        
    def chamar_nome(self):
            print (self.nome)
        
    def chamar_endereco_rua(self):
            print (self.rua)
            
p1 = Pessoa('91780-999', 'ipirangfa 241', 'vila nova', 'poa', 'jasmin da silva', 8798798, 6546546, 55)
p2 = Pessoa('88888-999', 'cap. amarantes xavier 241', 'campo novo', 'canoas', 'rodolfo da silva', 998798798, 996546546, 29)


            
            
       
   
        