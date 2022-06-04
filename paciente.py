from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, cpf, rg, idade, registro, historico):
        super(Paciente,self).__init__(nome, cpf, rg, idade)
        self.registro = registro
        self.historico = historico