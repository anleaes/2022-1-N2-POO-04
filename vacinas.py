class Vacinas:
    def __init__(self, n_serie, nome_vacina, data_fabricacao, dose, fabricante, doenca_tratar,quantidade):
        self.n_serie = n_serie
        self.nome_vacina = nome_vacina
        self.data_fabricacao = data_fabricacao
        self.dose = dose
        self.fabricante = fabricante
        self.doenca_tratar = doenca_tratar
        self.quantidade = quantidade
    def vacinas_fabricante(self):
        return print(self.fabricante)
    def vacinas_nome(self):
        return print(self.nome_vacina)
        


vac1 = Vacinas(99955, "gripezinha", '20_05_2021', "dose unica","fiocruz", 'covid19', 0) 
vac2 = Vacinas(77788, "malaria", '31_09_2022', "dose unica","fiocruz", 'covid19', 2)
 
     