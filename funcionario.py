from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, rg, idade, matricula):
        super(Funcionario,self).__init__(nome, cpf, rg, idade)
        self.matricula = matricula
        
        
    def ver_nome(self):
        print (self._pessoa._nome)
        