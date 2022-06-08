from pessoa import *

class Paciente:
    def __init__(self, pessoa, registro):
        #super(Paciente,self).__init__(nome, cpf, rg, idade)
        self.pessoa = pessoa
        self.registro = registro
        
        
pa01 = Paciente(p1, 999)
pa02 = Paciente(p2, 777)



