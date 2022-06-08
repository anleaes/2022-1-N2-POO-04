from paciente import Paciente
from pessoa import *
from posto import *
from paciente import *

class Agendamento_ficha:
    def __init__(self,pessoa, paciente, posto, nficha, data, horario):
        #super(Agendamento_ficha,self).__init__(nome, cpf, rg, idade)
        #super(Agendamento_ficha,self) .__init__(cep,rua,bairro,cidade)
        self.pessoa = pessoa
        self.paciente = paciente
        self.posto = posto
        self.nficha = nficha
        self.data = data
        self.horario = horario
        
    def endereco_posto_paciente(self):
        return print("o posto fica na rua: ", self.posto.endereco.rua)
    
    def diaehora_ficha(self):
        return print("horario marcado: ",self.horario, "data: ", self.data)
    
        
        
ficha001 = Agendamento_ficha(p1, pa01, posto01, 118,'12-02-2002', '18:32')
ficha002 = Agendamento_ficha(p2, pa02, posto02, 229,'31-03-2003', '17:44')
