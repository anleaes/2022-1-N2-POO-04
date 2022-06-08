from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, rg, idade, matricula):
        super(Funcionario,self).__init__(nome, cpf, rg, idade)
        self.matricula = matricula
        
        
    def ver_nome(self):
        print (self.nome)
        
func01 = Funcionario('rodrigo', 55555555, 44444444, 59, 656565)
func02 = Funcionario('CLABER', 222222, 999999, 99, 987998)

        