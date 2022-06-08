class CalendarioNacionalVacinacao:
    def __init__(self, crianca, adolescente, adulto, idosos):
        self.crianca = crianca
        self.adolescente = adolescente
        self.adulto = adulto
        self.idosos = idosos
    
    def calendario_nacional(self):
        return print(self.crianca, self.adolescente, self.adulto, self.idosos)

calendario2022 = CalendarioNacionalVacinacao ('Crianças: janeiro - 0 a 12anos','Adolescentes março - 12 a 17anos',' Adultos abril 18 a 59anos','Idosos maio 60 a 99anos' )
calendario2023 = CalendarioNacionalVacinacao ('Crianças: FEVEREIRO - 0 a 12anos','Adolescentes ABRIL - 12 a 17anos',' Adultos JUNHO 18 a 59anos','Idosos AGOSTO 60 a 99anos' )






            

    