from carteirinha_de_vacinacao import Carteirinha_de_vacinacao

class CalendarioNacionalVacinacao(Carteirinha_de_vacinacao):
    def __init__(self, crianca, adolescente, adulto, idosos):
        self.crianca = crianca
        self.adolescente = adolescente
        self.adulto = adulto
        self.idosos = idosos
        