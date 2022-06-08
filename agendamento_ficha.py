from paciente import Paciente
from posto import Posto

class Agendamento_ficha(Paciente, Posto):
    def __init__(self,nome, cpf, rg, idade, cep, rua,bairro,cidade, nficha, data, horario):
        super(Agendamento_ficha,self).__init__(nome, cpf, rg, idade)
        super(Agendamento_ficha,self) .__init__(cep,rua,bairro,cidade)
        self.nficha = nficha
        self.data = data
        self.horario = horario
        
    def endereco_posto_paciente(self):
        return print("o posto fica na rua %i ",self.rua)
    def horario_ficha(self):
        return print("o posto fica na rua %i",self.horario)
    def dia_consulta(self):
        return print(self.data)
        
        
ficha001 = Agendamento_ficha('veronica', '400.289.22', 558893, 18, '91790-850', 'voluntarios', 'centro', 'poa', 885,'12-02-2002', '18:32')
ficha002 = Agendamento_ficha('greice', '5573676', 558893, 33, '91766-66', 'andradas', 'joaquina', 'CANOAS', 886,'31-03-2003', '17:44')
