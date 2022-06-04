from paciente import Paciente
from posto import Posto

class Agendamento_ficha(Paciente, Posto):
    def __init__(self,nome, cpf, rg, idade, cep, rua,bairro,cidade, nficha, data, horario):
        super(Paciente,self).__init__(nome, cpf, rg, idade)
        super(Posto,self) .__init__(cep,rua,bairro,cidade)
        self.nficha = nficha
        self.data = data
        self.horario = horario