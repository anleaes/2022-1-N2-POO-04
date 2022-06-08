class Vacinas:
    def __init__(self, n_serie, nome, data_fabricacao, dose, fabricante, doenca_tratar,quantidade):
        self.n_serie = n_serie
        self.nome = nome
        self.data_fabricacao = data_fabricacao
        self.dose = dose
        self.fabricante = fabricante
        self.doenca_tratar = doenca_tratar
        self.quantidade = quantidade
        


vac1 = Vacinas(99955, "gripezinha", '20_05_2021', "dose unica","fiocruz", 'covid19', 0)  
     