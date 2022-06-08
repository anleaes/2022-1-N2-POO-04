from pessoa import *
from vacinas import *
from calendario_nacional_vacinacao import *


class Carteirinha_de_vacinacao:
    def __init__(self, pessoa, vacinas ,calendario_nacional_vacinacao ,registro):
        #super(Carteirinha_de_vacinacao,self).__init__(nome, cpf, rg, idade)
        #super(Carteirinha_de_vacinacao,self).__init__(self, nome_vacina, dose, fabricante, doenca_tratar)
        #super(Carteirinha_de_vacinacao,self).__init__(self, crianca, adolescente, adulto, idosos)
        self.pessoa = pessoa
        self.vacinas = vacinas
        self.calendario_nacional_vacinacao = calendario_nacional_vacinacao
        self.registro = registro
    
    def numero_carteirinha(self):
        return print(self.registro)
        
rc1 = Carteirinha_de_vacinacao(p1, vac1,calendario2022, 222 )
rc2 = Carteirinha_de_vacinacao(p2, vac2,calendario2023, 333 )


        
