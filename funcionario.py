from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, rg, idade, matricula):
        super(Funcionario,self).__init__(nome, cpf, rg, idade)
        self.matricula = matricula
        
        
    def ver_nome(self):
        print (self.nome)
    def numero_matricula(self):
        return print("o numero de matrícula do(a) funcionario(a)  %i ", self.nome, "é %i", self.matricula)
        
func01 = Funcionario('veronica', 55555555, 44444444, 59, 656565)

        