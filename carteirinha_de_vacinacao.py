from pessoa import Pessoa
from vacinas import Vacinas
from calendario_nacional_vacinacao import CalendarioNacionalVacinacao


class Carteirinha_de_vacinacao(Pessoa, Vacinas, CalendarioNacionalVacinacao):
    def __init__(self, nome, cpf, rg, idade, nome_vacina, dose, fabricante, doenca_tratar, crianca, adolescente, adulto, idosos):
        super(Carteirinha_de_vacinacao,self).__init__(nome, cpf, rg, idade)
        super(Carteirinha_de_vacinacao,self).__init__(self, nome_vacina, dose, fabricante, doenca_tratar)
        super(Carteirinha_de_vacinacao,self).__init__(self, crianca, adolescente, adulto, idosos)