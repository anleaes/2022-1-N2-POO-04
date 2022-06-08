from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, cpf, rg, idade, registro):
        super(Paciente,self).__init__(nome, cpf, rg, idade)
        self.registro = registro
        
        
pa01 = Paciente('greice', 6546546, 32132132, 32, 999)
