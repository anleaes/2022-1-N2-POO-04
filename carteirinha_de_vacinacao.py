from pessoa import Pessoa
from vacinas import Vacinas
from calendario_nacional_vacinacao import CalendarioNacionalVacinacao


class Carteirinha_de_vacinacao(Pessoa, Vacinas, CalendarioNacionalVacinacao):
    def __init__(self, nome, cpf, rg, idade, nome_vacina, dose, fabricante, doenca_tratar, crianca, adolescente, adulto, idosos,registro):
        super(Carteirinha_de_vacinacao,self).__init__(nome, cpf, rg, idade)
        super(Carteirinha_de_vacinacao,self).__init__(self, nome_vacina, dose, fabricante, doenca_tratar)
        super(Carteirinha_de_vacinacao,self).__init__(self, crianca, adolescente, adulto, idosos)
        self.registro = registro
    
    def numero_carteirinha(self):
        return print(self.registro)
        
rc1 = Carteirinha_de_vacinacao('veronica', '400.289.22', 558893, 18, 'sarampo', 1, 'china', 'sarampo', 'de 0 a 12anos', 'de 13 a 18anos', 'de 19 a 59anos', 'de 60 a 99 anos', 222 )
rc2 = Carteirinha_de_vacinacao('greice', '5573676', 558893, 33, 'CATAPORA', 2, 'EUA', 'CATAPORA', 'de 0 a 12anos', 'de 13 a 18anos', 'de 19 a 59anos', 'de 60 a 99 anos', 333 )


        
