from pessoa import *

class Funcionario:
    def __init__(self, pessoa, matricula):
        #super(Funcionario,self).__init__(nome, cpf, rg, idade)
        self.pessoa = pessoa
        self.matricula = matricula
        
        
    def ver_nome(self):
        print ("NOME DO FUNCIONÁRIO: ", self.pessoa.nome)
    def numero_matricula(self):
        return print("o numero de matrícula do(a) funcionario(a)  ", self.pessoa.nome, "é: ", self.matricula)
        
#func01 = Funcionario('veronica', 55555555, 44444444, 59, 656565)
func01 = Funcionario(p1, 5555555)
func02 = Funcionario(p2, 6666666)

        