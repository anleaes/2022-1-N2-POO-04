from paciente import Paciente
from posto import Posto

class Agendamento_ficha(Paciente, Posto):
    def __init__(self,nome, cpf, rg, idade, cep, rua,bairro,cidade, nficha, data, horario):
        super(Paciente,self).__init__(nome, cpf, rg, idade)
        super(Posto,self) .__init__(cep,rua,bairro,cidade)
        self.nficha = nficha
        self.data = data
        self.horario = horario
        
        
ficha001 = Agendamento_ficha('lucas', '898989', '90980241', 22, '91790-850', 'voluntarios', 'centro', 'poa', 885,'12-02-2002', '18:32')
ficha002 = Agendamento_ficha('diego', '77777', '9666666', 22, '91766-66', 'andradas', 'joaquina', 'CANOAS', 886,'31-03-2003', '17:44')
