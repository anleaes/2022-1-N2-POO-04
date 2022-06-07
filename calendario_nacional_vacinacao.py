class CalendarioNacionalVacinacao:
    def __init__(self, crianca, adolescente, adulto, idosos):
        self.crianca = crianca
        self.adolescente = adolescente
        self.adulto = adulto
        self.idosos = idosos
        
    

    @property
    def get_crianca(self):
        return self._crianca

    @get_crianca.setter
    def set_crianca(self, crianca):
        self._crianca = crianca
    
    @property
    def get_adolescente(self):
        return self._adolescente

    @get_adolescente.setter
    def set_adolescente(self, adolescente):
        self._adolescente = adolescente
    
    @property
    def get_adulto(self):
        return self._adulto

    @get_adulto.setter
    def set_adulto(self, adulto):
        self._adulto = adulto
        
    @property
    def get_idosos(self):
        return self._idosos

    @get_idosos.setter
    def set_idosos(self, idosos):
        self._idosos = idosos
        
calendario2022 = CalendarioNacionalVacinacao ('Crianças: janeiro - 0 a 12anos','Adolescentes março - 12 a 17anos',' Adultos abril 18 a 59anos','Idosos maio 60 a 99anos' )

print (calendario2022.crianca)

calendario2022.set_crianca = input(" teste teste : ")

print(calendario2022.get_crianca)






            

    